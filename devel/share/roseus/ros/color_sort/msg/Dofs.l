;; Auto-generated. Do not edit!


(when (boundp 'color_sort::Dofs)
  (if (not (find-package "COLOR_SORT"))
    (make-package "COLOR_SORT"))
  (shadow 'Dofs (find-package "COLOR_SORT")))
(unless (find-package "COLOR_SORT::DOFS")
  (make-package "COLOR_SORT::DOFS"))

(in-package "ROS")
;;//! \htmlinclude Dofs.msg.html


(defclass color_sort::Dofs
  :super ros::object
  :slots (_base _bs_to_f _f_to_s _s_to_thrd _claws ))

(defmethod color_sort::Dofs
  (:init
   (&key
    ((:base __base) 0)
    ((:bs_to_f __bs_to_f) 0)
    ((:f_to_s __f_to_s) 0)
    ((:s_to_thrd __s_to_thrd) 0)
    ((:claws __claws) 0)
    )
   (send-super :init)
   (setq _base (round __base))
   (setq _bs_to_f (round __bs_to_f))
   (setq _f_to_s (round __f_to_s))
   (setq _s_to_thrd (round __s_to_thrd))
   (setq _claws (round __claws))
   self)
  (:base
   (&optional __base)
   (if __base (setq _base __base)) _base)
  (:bs_to_f
   (&optional __bs_to_f)
   (if __bs_to_f (setq _bs_to_f __bs_to_f)) _bs_to_f)
  (:f_to_s
   (&optional __f_to_s)
   (if __f_to_s (setq _f_to_s __f_to_s)) _f_to_s)
  (:s_to_thrd
   (&optional __s_to_thrd)
   (if __s_to_thrd (setq _s_to_thrd __s_to_thrd)) _s_to_thrd)
  (:claws
   (&optional __claws)
   (if __claws (setq _claws __claws)) _claws)
  (:serialization-length
   ()
   (+
    ;; uint16 _base
    2
    ;; uint16 _bs_to_f
    2
    ;; uint16 _f_to_s
    2
    ;; uint16 _s_to_thrd
    2
    ;; uint16 _claws
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _base
       (write-word _base s)
     ;; uint16 _bs_to_f
       (write-word _bs_to_f s)
     ;; uint16 _f_to_s
       (write-word _f_to_s s)
     ;; uint16 _s_to_thrd
       (write-word _s_to_thrd s)
     ;; uint16 _claws
       (write-word _claws s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _base
     (setq _base (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _bs_to_f
     (setq _bs_to_f (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _f_to_s
     (setq _f_to_s (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _s_to_thrd
     (setq _s_to_thrd (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _claws
     (setq _claws (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get color_sort::Dofs :md5sum-) "be6b4ca6915145d1e914b71d6acb81cd")
(setf (get color_sort::Dofs :datatype-) "color_sort/Dofs")
(setf (get color_sort::Dofs :definition-)
      "uint16 base
uint16 bs_to_f
uint16 f_to_s
uint16 s_to_thrd
uint16 claws

")



(provide :color_sort/Dofs "be6b4ca6915145d1e914b71d6acb81cd")


