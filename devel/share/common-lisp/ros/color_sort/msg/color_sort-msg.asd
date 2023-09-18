
(cl:in-package :asdf)

(defsystem "color_sort-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Dofs" :depends-on ("_package_Dofs"))
    (:file "_package_Dofs" :depends-on ("_package"))
  ))