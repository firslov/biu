;; a snails backend for biu
(require 'snails-core)

(defvar biu-commands
  (split-string (substring (shell-command-to-string "biu list")
                           0 -1) "\n"))

(snails-create-sync-backend
 :name
 "BIU"

 :candidate-filter
 (lambda (input)
   (let (candidates)
     (dolist (file biu-commands)
       (when (or
              (string-equal input "")
              (string-match-p (regexp-quote input) file))
         (snails-add-candiate 'candidates (snails-wrap-file-icon file) file)))
     candidates))

 :candiate-do
 (lambda (candidate)
   (start-process (concat (list "biu " candidate)))))

(provide 'snails-backend-biu)
