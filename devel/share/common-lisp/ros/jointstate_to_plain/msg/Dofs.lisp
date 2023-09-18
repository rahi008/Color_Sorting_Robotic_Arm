; Auto-generated. Do not edit!


(cl:in-package jointstate_to_plain-msg)


;//! \htmlinclude Dofs.msg.html

(cl:defclass <Dofs> (roslisp-msg-protocol:ros-message)
  ((base
    :reader base
    :initarg :base
    :type cl:fixnum
    :initform 0)
   (bs_to_f
    :reader bs_to_f
    :initarg :bs_to_f
    :type cl:fixnum
    :initform 0)
   (f_to_s
    :reader f_to_s
    :initarg :f_to_s
    :type cl:fixnum
    :initform 0)
   (s_to_thrd
    :reader s_to_thrd
    :initarg :s_to_thrd
    :type cl:fixnum
    :initform 0)
   (claws
    :reader claws
    :initarg :claws
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Dofs (<Dofs>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Dofs>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Dofs)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name jointstate_to_plain-msg:<Dofs> is deprecated: use jointstate_to_plain-msg:Dofs instead.")))

(cl:ensure-generic-function 'base-val :lambda-list '(m))
(cl:defmethod base-val ((m <Dofs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jointstate_to_plain-msg:base-val is deprecated.  Use jointstate_to_plain-msg:base instead.")
  (base m))

(cl:ensure-generic-function 'bs_to_f-val :lambda-list '(m))
(cl:defmethod bs_to_f-val ((m <Dofs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jointstate_to_plain-msg:bs_to_f-val is deprecated.  Use jointstate_to_plain-msg:bs_to_f instead.")
  (bs_to_f m))

(cl:ensure-generic-function 'f_to_s-val :lambda-list '(m))
(cl:defmethod f_to_s-val ((m <Dofs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jointstate_to_plain-msg:f_to_s-val is deprecated.  Use jointstate_to_plain-msg:f_to_s instead.")
  (f_to_s m))

(cl:ensure-generic-function 's_to_thrd-val :lambda-list '(m))
(cl:defmethod s_to_thrd-val ((m <Dofs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jointstate_to_plain-msg:s_to_thrd-val is deprecated.  Use jointstate_to_plain-msg:s_to_thrd instead.")
  (s_to_thrd m))

(cl:ensure-generic-function 'claws-val :lambda-list '(m))
(cl:defmethod claws-val ((m <Dofs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jointstate_to_plain-msg:claws-val is deprecated.  Use jointstate_to_plain-msg:claws instead.")
  (claws m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Dofs>) ostream)
  "Serializes a message object of type '<Dofs>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'base)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'base)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'bs_to_f)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'bs_to_f)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'f_to_s)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'f_to_s)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 's_to_thrd)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 's_to_thrd)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'claws)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'claws)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Dofs>) istream)
  "Deserializes a message object of type '<Dofs>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'base)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'base)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'bs_to_f)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'bs_to_f)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'f_to_s)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'f_to_s)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 's_to_thrd)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 's_to_thrd)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'claws)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'claws)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Dofs>)))
  "Returns string type for a message object of type '<Dofs>"
  "jointstate_to_plain/Dofs")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Dofs)))
  "Returns string type for a message object of type 'Dofs"
  "jointstate_to_plain/Dofs")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Dofs>)))
  "Returns md5sum for a message object of type '<Dofs>"
  "be6b4ca6915145d1e914b71d6acb81cd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Dofs)))
  "Returns md5sum for a message object of type 'Dofs"
  "be6b4ca6915145d1e914b71d6acb81cd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Dofs>)))
  "Returns full string definition for message of type '<Dofs>"
  (cl:format cl:nil "uint16 base~%uint16 bs_to_f~%uint16 f_to_s~%uint16 s_to_thrd~%uint16 claws~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Dofs)))
  "Returns full string definition for message of type 'Dofs"
  (cl:format cl:nil "uint16 base~%uint16 bs_to_f~%uint16 f_to_s~%uint16 s_to_thrd~%uint16 claws~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Dofs>))
  (cl:+ 0
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Dofs>))
  "Converts a ROS message object to a list"
  (cl:list 'Dofs
    (cl:cons ':base (base msg))
    (cl:cons ':bs_to_f (bs_to_f msg))
    (cl:cons ':f_to_s (f_to_s msg))
    (cl:cons ':s_to_thrd (s_to_thrd msg))
    (cl:cons ':claws (claws msg))
))
