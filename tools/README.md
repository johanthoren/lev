# Instructions for usfm-mode.el
Add the following, or similar, to somewhere reasonable - such as init.el:
```
;; USFM related below.
(add-to-list 'load-path "~/.emacs.d/private/lisp/usfm")
(require 'usfm-mode)
(autoload 'usfm-mode "usfm" "A major mode to add color coding to usfm formatted files." t)
(add-to-list 'auto-mode-alist '("\\.usfm\\'" . usfm-mode))
;; Fix text to always display left-to-right.
(add-hook 'usfm-mode-hook (lambda ()
                            (setq bidi-paragraph-direction 'left-to-right)
                            (setq truncate-lines t)
                            ))
```

Copy `usfm-mode.el` to the specified load-path above.
