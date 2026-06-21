(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cadar x) (car (cdr (car x))))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 14
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 14
  (define (helper s c)
    (if (null? s)
      '()
      (cons (list c (car s)) (helper (cdr s) (+ c 1)))))
  (helper s 0))
  ; END PROBLEM 14
  


;; Problem 15

;; Return the value for a key in a dictionary list
(define (get dict key)
  ; BEGIN PROBLEM 15
  (cond
    ((null? dict) #f)
    ((equal? (car (car dict)) key) (car (cdr (car dict))))
    (else (get (cdr dict) key))))
  ; END PROBLEM 15
  

;; Return a dictionary list with a (key value) pair
(define (set dict key val)
    (cond
      ((null? dict) (cons (list key val) '()))
      ((equal? (car (car dict)) key) (cons (list key val) (cdr dict)))
      (else (cons (list (car (car dict)) (car (cdr (car dict)))) (set (cdr dict) key val)))))
  ; BEGIN PROBLEM 15
  ; END PROBLEM 15
  

;; Problem 16

;; implement solution-code
(define (solution-code problem solution)
  ; BEGIN PROBLEM 16
  (cond ((null? problem) '())
        ((not (pair? problem)) (if (equal? problem '_____) solution problem))
        (else (cons (solution-code (car problem) solution) (solution-code (cdr problem) solution)))))
  ; END PROBLEM 16
  
