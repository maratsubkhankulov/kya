#include <new>
#include <iostream>
#include <cstdlib>

void out_of_mem() {
    std::cerr << "Unable to satisfy request for memory\n";
    std::abort();
}

int main() {
    std::set_new_handler(out_of_mem);
    int* big_array = new int[1000000000000000L];
}
