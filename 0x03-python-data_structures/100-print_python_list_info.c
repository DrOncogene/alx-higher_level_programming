#include "Python.h"

void print_python_list_info(PyObject *p)
{
	long long i, size;
	PyListObject *the_list = (PyListObject *)p;

	size = (long long)Py_SIZE(p);
	printf("[*] Size of the Python List = %lld\n", size);
	printf("[*] Allocated = %lld\n", (long long)the_list->allocated);
	for (i = 0; i < size; i++){
		printf("Element %lld: %s\n", i, Py_TYPE(the_list->ob_item[i])->tp_name);
	}
}
