#include <Python.h>

/**
 * print_python_list_info - print info about python list
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int s, a, j;
	PyObject *ob;

	s = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (j = 0; j < s; j++)
	{
		printf("Element %d: ", j);
		ob = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
