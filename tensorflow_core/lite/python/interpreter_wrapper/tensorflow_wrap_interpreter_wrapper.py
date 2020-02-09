# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_tensorflow_wrap_interpreter_wrapper', [dirname(__file__)])
        except ImportError:
            import _tensorflow_wrap_interpreter_wrapper
            return _tensorflow_wrap_interpreter_wrapper
        if fp is not None:
            try:
                _mod = imp.load_module('_tensorflow_wrap_interpreter_wrapper', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _tensorflow_wrap_interpreter_wrapper = swig_import_helper()
    del swig_import_helper
else:
    import _tensorflow_wrap_interpreter_wrapper
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def PyListToStdVectorString(list, strings):
    return _tensorflow_wrap_interpreter_wrapper.PyListToStdVectorString(list, strings)
PyListToStdVectorString = _tensorflow_wrap_interpreter_wrapper.PyListToStdVectorString
class InterpreterWrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, InterpreterWrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, InterpreterWrapper, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _tensorflow_wrap_interpreter_wrapper.delete_InterpreterWrapper
    __del__ = lambda self: None

    def AllocateTensors(self):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_AllocateTensors(self)

    def Invoke(self):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_Invoke(self)

    def InputIndices(self):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_InputIndices(self)

    def OutputIndices(self):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_OutputIndices(self)

    def ResizeInputTensor(self, i, value):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_ResizeInputTensor(self, i, value)

    def NumTensors(self):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_NumTensors(self)

    def TensorName(self, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_TensorName(self, i)

    def TensorType(self, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_TensorType(self, i)

    def TensorSize(self, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_TensorSize(self, i)

    def TensorQuantization(self, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_TensorQuantization(self, i)

    def SetTensor(self, i, value):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_SetTensor(self, i, value)

    def GetTensor(self, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_GetTensor(self, i)

    def ResetVariableTensors(self):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_ResetVariableTensors(self)

    def NumNodes(self):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_NumNodes(self)

    def NodeName(self, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_NodeName(self, i)

    def NodeInputs(self, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_NodeInputs(self, i)

    def NodeOutputs(self, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_NodeOutputs(self, i)

    def tensor(self, base_object, i):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_tensor(self, base_object, i)

    def ModifyGraphWithDelegate(self, delegate):
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_ModifyGraphWithDelegate(self, delegate)
    __swig_getmethods__["CreateWrapperCPPFromFile"] = lambda x: _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromFile
    if _newclass:
        CreateWrapperCPPFromFile = staticmethod(_tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromFile)
    __swig_getmethods__["CreateWrapperCPPFromBuffer"] = lambda x: _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromBuffer
    if _newclass:
        CreateWrapperCPPFromBuffer = staticmethod(_tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromBuffer)
InterpreterWrapper_swigregister = _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_swigregister
InterpreterWrapper_swigregister(InterpreterWrapper)

def InterpreterWrapper_CreateWrapperCPPFromFile(*args):
    return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromFile(*args)
InterpreterWrapper_CreateWrapperCPPFromFile = _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromFile

def InterpreterWrapper_CreateWrapperCPPFromBuffer(*args):
    return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromBuffer(*args)
InterpreterWrapper_CreateWrapperCPPFromBuffer = _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_CreateWrapperCPPFromBuffer

# This file is compatible with both classic and new-style classes.


