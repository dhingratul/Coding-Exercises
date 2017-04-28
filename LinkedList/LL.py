#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:08:35 2017

@author: dhingratul
"""

class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
    
class LinkedList:
    def __init__(self):
        self.head=None;
        
# Print the linkedList        
    def printList(self):
        temp=self.head;
        while(temp):
            print(temp.data);
            temp=temp.next;     
# pUsh to first    
    def push(self,new_data):
        new_node=Node(new_data);
        new_node.next=self.head;             
        self.head=new_node;
        
    def insertAfter(self,prev_node, new_data):
        new_node=Node(new_data);
        if prev_node is None:
            print('Use push method');
            return;
        prev_node.next=new_node;
        new_node.next=prev_node.next;       
        
    def append(self,new_data):
        new_node=Node(new_data);
        # If  the list is empty
        if self.head is None:
            self.head=new_node;
            return
        last=self.head;
        while(last.next):
            last=last.next;
        last.next=new_node;    
                                          
if __name__=='__main__':
    # Empty LL
    llist=LinkedList();
# Here the data is 1,2,3                    
    #llist.head=Node(1);
    #second=Node(2);
    #third=Node(3);
    #llist.head.next=second;
    #second.next=third;
    
    llist.append(6);
    llist.push(5);
    llist.push(1);       
#    llist.insertAfter(llist.head.next, 8)          
    llist.printList();
    
                 