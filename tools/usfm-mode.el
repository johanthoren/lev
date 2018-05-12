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
        ("\\(\\\\ft[[:space:]]\\)\\(.*\\)\\(\\\\f\\*[[:space:]]\\)" . font-lock-negation-char-face)
        ("\\\\fk[[:space:]]\\|\\\\fr[[:space:]]\\|\\\\ft[[:space:]]\\|\\\\f\\*[[:space:]]\\|\\\\f[[:space:]]" . font-lock-keyword-face)
        ("\\\\ide[[:space:]]\\|\\\\id[[:space:]]\\|\\\\toc[0-3][[:space:]]\\|\\\\mt[0-3][[:space:]]\\|\\\\sts[[:space:]]\\|\\\\rem[[:space:]]" . font-lock-type-face)
        ("\\\\q[1-3][[:space:]]" . font-lock-constant-face)
        ("\\\\d[[:space:]]" . font-lock-constant-face)
        ("\\\\qs\\*\\|[[:space:]]\\\\qs[[:space:]]" . font-lock-constant-face)
        ("\\\\qa\\*\\|[[:space:]]\\\\qa[[:space:]]" . font-lock-constant-face)
        ("\\\\add\\*\\|[[:space:]]\\\\add[[:space:]]" . font-lock-constant-face)
        ("\\\\ms[[:space:]]\\|\\\\s[1-3][[:space:]]\\|\\\\p\\|\\\\b" . font-lock-variable-name-face)
        ))

(define-derived-mode usfm-mode text-mode "usfm"
  "major mode for editing usfm language code."
  (setq font-lock-defaults '(usfm-highlights)))

(provide 'usfm-mode)

;;; usfm-mode.el ends here
