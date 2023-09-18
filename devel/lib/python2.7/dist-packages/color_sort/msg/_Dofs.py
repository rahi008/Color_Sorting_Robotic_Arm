# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from color_sort/Dofs.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Dofs(genpy.Message):
  _md5sum = "be6b4ca6915145d1e914b71d6acb81cd"
  _type = "color_sort/Dofs"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint16 base
uint16 bs_to_f
uint16 f_to_s
uint16 s_to_thrd
uint16 claws
"""
  __slots__ = ['base','bs_to_f','f_to_s','s_to_thrd','claws']
  _slot_types = ['uint16','uint16','uint16','uint16','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       base,bs_to_f,f_to_s,s_to_thrd,claws

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Dofs, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.base is None:
        self.base = 0
      if self.bs_to_f is None:
        self.bs_to_f = 0
      if self.f_to_s is None:
        self.f_to_s = 0
      if self.s_to_thrd is None:
        self.s_to_thrd = 0
      if self.claws is None:
        self.claws = 0
    else:
      self.base = 0
      self.bs_to_f = 0
      self.f_to_s = 0
      self.s_to_thrd = 0
      self.claws = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_5H().pack(_x.base, _x.bs_to_f, _x.f_to_s, _x.s_to_thrd, _x.claws))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 10
      (_x.base, _x.bs_to_f, _x.f_to_s, _x.s_to_thrd, _x.claws,) = _get_struct_5H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_5H().pack(_x.base, _x.bs_to_f, _x.f_to_s, _x.s_to_thrd, _x.claws))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 10
      (_x.base, _x.bs_to_f, _x.f_to_s, _x.s_to_thrd, _x.claws,) = _get_struct_5H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_5H = None
def _get_struct_5H():
    global _struct_5H
    if _struct_5H is None:
        _struct_5H = struct.Struct("<5H")
    return _struct_5H
