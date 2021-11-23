#include <Python.h>

void
print_python_list_info(PyObject *p)
{
	long long i, size;
	PyObject *item;
	PyListObject *the_list = (PyListObject *)p;

	size = PyList_Size(p);
	printf("[*] Size of the python list = %lld\n", size);
	printf("[*] Allocated = %lld\n", (long long)the_list->allocated);
	for (i = 0; i < size; i++){
		item = PyList_GetItem(p, i);
		printf("Element %lld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
