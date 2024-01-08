#include <stdio.h>
#include "Python.h"

/**
 * print_python_string: prints Python strings.
 * @p: the python object
 * Return: nothing
 */


void print_python_string(PyObject *p)
{
    int length = 0;
    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("p is not a valid string");
        return;
    }

    length = ((PyASCIIObject *)p)->length;

    if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
