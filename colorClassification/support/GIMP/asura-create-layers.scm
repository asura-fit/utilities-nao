;;;; asura-create-layers for GIMP 2.x

(define +asura-layers+ '("Ignore"
                         "Background"
                         "White"
                         "Red"
                         "Blue"
                         "Yellow"
                         "Green"
                         "Cyan"
                         "Ball"))
(define +asura-color-ignore+
  (car (gimp-palette-entry-get-color "AsuraColor" 10)))

(define (create-layer img name w h)
  (gimp-image-add-layer img
                        (car (gimp-layer-new img w h 1 name 100 0))
                        -1))

(define (create-layers namelis img w h)
  (if (not (null? namelis))
      (begin (create-layer img (car namelis) w h)
             (create-layers (cdr namelis) img w h))))

(define (asura-create-layers img)
  (let ((w (car (gimp-image-width img)))
        (h (car (gimp-image-height img))))
    (create-layers +asura-layers+ img w h)
    (let ((layer-ignore
           (car (gimp-image-get-layer-by-name img "Ignore"))))
      (gimp-context-set-foreground +asura-color-ignore+)
      (gimp-drawable-fill layer-ignore 0)
      (gimp-layer-set-visible layer-ignore FALSE))))


;;;; register to GIMP as Script-Fu
(script-fu-register
 "asura-create-layers"                  ; func name
;"CreateLayers"                         ; menu label
 "Create asura layers"                  ; menu label
 "Creates asura-color layers"           ; description
 "sin @ ASURA-FIT"                      ; author
 "copyright 2008, sin @ Asura-FIT"      ; copyright notice
 "December 19, 2008"                    ; date created
 ""                     ;image type that the script works on
 SF-IMAGE
 "Image:"
 0) ;a string variable
 

;;;; (script-fu-menu-register "asura-create-layers" "<Toolbox>/Xtns/Asura")
(script-fu-menu-register "asura-create-layers" "<Toolbox>/Xtns/")

