;;; usfm-mode.el -*- coding: utf-8; lexical-binding: t; -*-

;; Copyright © 2018, by Johan Thorén

;; Author: Johan Thorén <johan@thoren.xyz>
;; Version: 0.1.0
;; Created: 4 April 2018
;; Keywords: languages

;; This file is not part of GNU Emacs.

;;; License:

;; You can redistribute this program and/or modify it under the terms of the GNU General Public License version 2.

;;; Commentary:

;;; A mode to provide syntax color for usfm files.

;;; Code:

(setq usfm-highlights
      '(("\\\\v[[:space:]][1-9][0-9][0-9]\\|\\\\v[[:space:]][1-9][0-9]\\|\\\\v[[:space:]][1-9]" . font-lock-function-name-face)
        ("\\\\c[[:space:]][1-9][0-9][0-9]\\|\\\\c[[:space:]][1-9][0-9]\\|\\\\c[[:space:]][1-9]" . font-lock-keyword-face)
        ("\\(\\\\ft[[:space:]]\\)\\(.*\\)\\(\\\\f\\*\\)" . font-lock-negation-char-face)
        ("\\\\fk\\|\\\\fr\\|\\\\ft\\|\\\\f\\*\\|\\\\f" . font-lock-keyword-face)
        ("\\\\ide\\|\\\\id\\|\\\\toc[0-3]\\|\\\\mt[0-3]\\|\\\\sts\\|\\\\rem" . font-lock-type-face)
        ("\\\\q[1-3]" . font-lock-constant-face)
        ("\\\\add\\*\\|\\\\add[[:space:]]" . font-lock-constant-face)
        ("\\\\ms\\|\\\\s[1-3]\\|\\\\p\\|\\\\b" . font-lock-variable-name-face)
        ))

(define-derived-mode usfm-mode text-mode "usfm"
  "major mode for editing usfm language code."
  (setq font-lock-defaults '(usfm-highlights)))

(provide 'usfm-mode)

;;; usfm-mode.el ends here
