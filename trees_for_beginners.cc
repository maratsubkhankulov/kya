#include "stdio.h"
#include <string>

class Node {
    // ctor
    Node(Node left, Node right, std::string data):
       _left(left),
       _right(right),
       _data(data)
    {}

    Node _left;
    Node _right;
    std::string _data;
}

void main(int n_args, char* args) {
    std::cout << "hello world";
}
