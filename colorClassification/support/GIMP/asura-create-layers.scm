;Creates layers for Color Classification on Gimp2
;For TinyScheme on GIMP
;ver 0.42


;create a layer
(define (create-layer img name w h)
	(;let* (
		)
		;(define layer (car (gimp-layer-new img w h 1 name 100 0)))
		(gimp-image-add-layer img
			(car (gimp-layer-new img w h 1 name 100 0)) -1
		;)
	)
)


;main funktion
;
(define (asura-create-layers image)
	(let* (
;			old asura colour
;			(layer-name ("Ignore" "Background" "Field [reserved]" "White" "Red" "Blue" "Pink" "Yellow" "Green" "Cyan" "Ball"))
;			new asura colour
			(layer-name (list "Ignore" "Background" "White" "Red" "Blue" "Yellow" "Green" "Cyan" "Ball"))

			(ignore (car (gimp-palette-entry-get-color "AsuraColor" 10)))
			(width (car (gimp-image-width image)))
			(height (car (gimp-image-height image)))
		)

			(create-layer image "Ignore" width height)
			(define drw (car (gimp-image-get-active-drawable image)))
			(gimp-context-set-foreground ignore)
			(gimp-drawable-fill drw 0)
			(gimp-drawable-set-visible drw FALSE)

;loop test
;			(do (list (cdr layer-name) (cdr list))
;				(null? list)
;				(create-layer image (car list) width height)
;			)

			(create-layer image "Background" width height)
			(create-layer image "White" width height)
			(create-layer image "Red" width height)
			(create-layer image "Blue" width height)
			(create-layer image "Yellow" width height)
			(create-layer image "Green" width height)
			(create-layer image "Cyan" width height)
			(create-layer image "Ball" width height)
	)
)


;register to Script-Fu
(script-fu-register
	"asura-create-layers"                     ;func name
;	"CreateLayers"              ;menu label
	"Asura CreateLayers"              ;menu label
	"Creates asura-color layers"              ;description
	"sin @ ASURA-FIT"                         ;author
	"copyright 2008, sin @ Asura-FIT"         ;copyright notice
	"December 19, 2008"                       ;date created
	""                     ;image type that the script works on
	SF-IMAGE      "Image:"         0   ;a string variable
)

;(script-fu-menu-register "asura-create-layers" "<Toolbox>/Xtns/Asura")
(script-fu-menu-register "asura-create-layers" "<Toolbox>/Xtns/")