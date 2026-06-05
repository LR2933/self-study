(define (ascending? s)
  (cond
    ((null? s) #t)
    ((null? (cdr s)) #t)
    ((<= (car s) (car(cdr s))) (ascending? (cdr s)))
    (else #f)
  )
)

(define (my-filter pred s)
  (cond 
    ((null? s) '())
    ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
    (else (my-filter pred (cdr s)))
  )
)

(define (interleave lst1 lst2) 'YOUR-CODE-HERE)

(define (no-repeats s) 'YOUR-CODE-HERE)
