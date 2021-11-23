#include "Python.h"

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;
	PyListObject *the_list = (PyListObject *)p;

	size = PyList_Size(p);
	printf("[*] Size of the python list = %ld\n", size);
	printf("[*] Allocated = %ld\n", the_list->allocated);
	for (i = 0; i < size; i++){
		printf("Element %ld: %s\n", i, Py_TYPE(the_list->ob_item[i])->tp_name);
	}
}
