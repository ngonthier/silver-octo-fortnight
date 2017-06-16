#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TestFFT2D.py
#  
#  Copyright 2017 Nicolas <nicolas@Clio>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  The goal of that script is to show error due to the CPU->GPU memcpy in 
#  CUDA used by Tensorflow


import tensorflow as tf
import numpy as np

def get_loss(sess,net,img_ref,layer):
    
    total_loss  = 0.
    
    sess.run(net['input'].assign(img_ref))  
    x = net[layer]
    a = sess.run(net[layer])
    x = tf.transpose(x, [0,3,1,2])
    a = tf.transpose(a, [0,3,1,2])
    _,N,_,_ = a.shape
    F_x = tf.fft2d(tf.complex(x,0.))
    F_x_conj = tf.conj(F_x)
    F_a = tf.fft2d(tf.complex(a,0.))
    F_a_conj = tf.conj(F_a)
    
    N = 1
    
    for i in range(N):
        inter_corr_x = tf.multiply(F_x,F_x_conj)
        inter_corr_a = tf.multiply(F_a,F_a_conj)
        
        ifft2_corr_x = tf.ifft2d(inter_corr_x)
        ifft2_corr_a = tf.ifft2d(inter_corr_a)
        
        R_x = tf.real(ifft2_corr_x)
        R_a = tf.real(ifft2_corr_a)
        
        style_loss = tf.nn.l2_loss(tf.subtract(R_x,R_a))  
        total_loss += style_loss
        
        # Shift the tensor from on 1 unit on the dimension 1
        F_x = tf.concat([tf.expand_dims(F_x[:,-1,:,:],0), F_x[:,:-1,:,:]], axis=1)
        F_a = tf.concat([tf.expand_dims(F_a[:,-1,:,:],0), F_a[:,:-1,:,:]], axis=1)
            
    return(total_loss)

def main(args):
    
    # Definition of the first operations :
    height, width, numberChannels = 400,300,3
    net = {}
    current = tf.Variable(np.zeros((1, height, width, numberChannels), dtype=np.float32))
    net['input'] = current
    kernel = tf.constant(np.random.uniform(low=-1,high=1,size=(400,300,3,64)),dtype=np.float32)
    conv = tf.nn.conv2d(current, kernel, strides=(1, 1, 1, 1),padding='SAME',name='conv')
    bias = tf.constant(np.random.uniform(low=-1,high=1,size=(64)),dtype=np.float32)
    conv_add_bias = tf.nn.bias_add(conv, bias)
    net['conv1_1'] = conv_add_bias
    
    img_ref = np.random.uniform(low=-128,high=128,size=(1, height, width, numberChannels))
    init_img = np.random.uniform(low=-128,high=128,size=(1, height, width, numberChannels))
    
    sess = tf.Session()
    
    sess.run(net['input'].assign(img_ref))  
    # Definition of the loss 
    loss = get_loss(sess,net,img_ref,'conv1_1')
        
    # Preparation of the assignation operation
    placeholder = tf.placeholder(tf.float32, shape=init_img.shape)
    assign_op = net['input'].assign(placeholder)
        
    sess.run(tf.global_variables_initializer())
    sess.run(assign_op, {placeholder: init_img})
    print("Before loss evaluation")
    loss_evaluation = sess.run(loss)
    print("loss_evaluation",loss_evaluation)
    
    return(0)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
