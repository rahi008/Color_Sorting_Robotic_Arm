// Auto-generated. Do not edit!

// (in-package jointstate_to_plain.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Dofs {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.base = null;
      this.bs_to_f = null;
      this.f_to_s = null;
      this.s_to_thrd = null;
      this.claws = null;
    }
    else {
      if (initObj.hasOwnProperty('base')) {
        this.base = initObj.base
      }
      else {
        this.base = 0;
      }
      if (initObj.hasOwnProperty('bs_to_f')) {
        this.bs_to_f = initObj.bs_to_f
      }
      else {
        this.bs_to_f = 0;
      }
      if (initObj.hasOwnProperty('f_to_s')) {
        this.f_to_s = initObj.f_to_s
      }
      else {
        this.f_to_s = 0;
      }
      if (initObj.hasOwnProperty('s_to_thrd')) {
        this.s_to_thrd = initObj.s_to_thrd
      }
      else {
        this.s_to_thrd = 0;
      }
      if (initObj.hasOwnProperty('claws')) {
        this.claws = initObj.claws
      }
      else {
        this.claws = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Dofs
    // Serialize message field [base]
    bufferOffset = _serializer.uint16(obj.base, buffer, bufferOffset);
    // Serialize message field [bs_to_f]
    bufferOffset = _serializer.uint16(obj.bs_to_f, buffer, bufferOffset);
    // Serialize message field [f_to_s]
    bufferOffset = _serializer.uint16(obj.f_to_s, buffer, bufferOffset);
    // Serialize message field [s_to_thrd]
    bufferOffset = _serializer.uint16(obj.s_to_thrd, buffer, bufferOffset);
    // Serialize message field [claws]
    bufferOffset = _serializer.uint16(obj.claws, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Dofs
    let len;
    let data = new Dofs(null);
    // Deserialize message field [base]
    data.base = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [bs_to_f]
    data.bs_to_f = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [f_to_s]
    data.f_to_s = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [s_to_thrd]
    data.s_to_thrd = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [claws]
    data.claws = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 10;
  }

  static datatype() {
    // Returns string type for a message object
    return 'jointstate_to_plain/Dofs';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'be6b4ca6915145d1e914b71d6acb81cd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint16 base
    uint16 bs_to_f
    uint16 f_to_s
    uint16 s_to_thrd
    uint16 claws
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Dofs(null);
    if (msg.base !== undefined) {
      resolved.base = msg.base;
    }
    else {
      resolved.base = 0
    }

    if (msg.bs_to_f !== undefined) {
      resolved.bs_to_f = msg.bs_to_f;
    }
    else {
      resolved.bs_to_f = 0
    }

    if (msg.f_to_s !== undefined) {
      resolved.f_to_s = msg.f_to_s;
    }
    else {
      resolved.f_to_s = 0
    }

    if (msg.s_to_thrd !== undefined) {
      resolved.s_to_thrd = msg.s_to_thrd;
    }
    else {
      resolved.s_to_thrd = 0
    }

    if (msg.claws !== undefined) {
      resolved.claws = msg.claws;
    }
    else {
      resolved.claws = 0
    }

    return resolved;
    }
};

module.exports = Dofs;
