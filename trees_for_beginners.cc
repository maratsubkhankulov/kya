//#include <stdio.h>
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Node {
public:
    // ctor
    Node(std::string data, Node* left, Node* right):
       _data(data),
       _left(left),
       _right(right)
    {}

    ~Node() {
        delete _left;
        delete _right;
    }

    std::string _data;
    Node* _left;
    Node* _right;
};

Node* create_tree() {
    // Create tree
    Node* tree = new Node("a", new Node("b", NULL, NULL), new Node("c", NULL, NULL));

    // Edit tree
    tree->_left->_left = new Node("d", NULL, NULL);
    tree->_left->_right = new Node("e", NULL, NULL);
    tree->_right->_left = new Node("f", NULL, NULL);
    tree->_right->_right = new Node("g", NULL, NULL);

    return tree;
}

void in_order(const Node* tree) {
    if (tree != NULL) {
        in_order(tree->_left);
        // Visit
        cout << tree->_data << std::endl;
        in_order(tree->_right);
    }
}

void pre_order(const Node* tree) {
    if (tree != NULL) {
        // Visit
        cout << tree->_data << std::endl;
        pre_order(tree->_left);
        pre_order(tree->_right);
    }
}

void post_order(const Node* tree) {
    if (tree != NULL) {
        post_order(tree->_left);
        post_order(tree->_right);
        // Visit
        cout << tree->_data << std::endl;
    }
}

void level_order(const Node* tree) {
    if (tree == NULL) {
        cout << "root is null";
        return;
    }
    deque<const Node*> queue;
    queue.push_front(tree);
    while (queue.size() > 0) {
        const Node* node = queue.back();
        queue.pop_back();
        cout << node->_data << std::endl;
        if (node->_left != NULL) {
            queue.push_front(node->_left);
        }
        if (node->_right != NULL) {
            queue.push_front(node->_right);
        }
    }
}

int tree_height(const Node* node, int depth)
{
    if (node != NULL) {
        // Go left
        int left_height = tree_height(node->_left, depth + 1);
        // Go right
        int right_height = tree_height(node->_right, depth + 1);
        return max(left_height, right_height);
    } else {
        return depth;
    }
}

int num_leaves(const Node* node, int count)
{
    if (node != NULL) {
        // Go left
        count = num_leaves(node->_left, count);
        // Go right
        count = num_leaves(node->_right, count);
        if (node->_left == NULL and node->_right == NULL) {
            count += 1;
        }
    }
    return count;
}

void pre_order_print(const Node* node, int depth)
{
    if (node != NULL) {
        // Visit
        cout << string(4 * depth, ' ') << node->_data << endl;
        // Go left
        pre_order_print(node->_left, depth + 1);
        // Go right
        pre_order_print(node->_right, depth + 1);
    }
}

int main(int n_args, char** args) {

    cout << "Create tree\n";
    Node* tree = create_tree();

    cout << "in order\n";
    in_order(tree);
    cout << "pre order\n";
    pre_order(tree);
    cout << "post order\n";
    post_order(tree);
    cout << "level order\n";
    level_order(tree);

    cout << "tree height: " << tree_height(tree, 0) << endl;
    cout << "num leaves: " << num_leaves(tree, 0) << endl;
    cout << "pre order print\n";
    pre_order_print(tree, 0);

    return 0;
}
