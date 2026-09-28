(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cadar x) (car (cdr (car x))))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 14
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 14
  (define (enumerate_new s n) 
    (if (null? s)
      nil
      (cons (list n (car s)) (enumerate_new (cdr s) (+ n 1)))
  )
  )
  (enumerate_new s 0)
  ; END PROBLEM 14
  )


;; Problem 15

;; Return the value for a key in a dictionary list
(define (get dict key)
  ; BEGIN PROBLEM 15
  (if (null? dict)
    #f
    (if (equal? key (caar dict))
    (car (cdar dict))
    (get (cdr dict) key)
  )
  )
  ; END PROBLEM 15
  )

;; Return a dictionary list with a (key value) pair
(define (set dict key val)
  ; BEGIN PROBLEM 15
  (if (null? dict)
    (list (list key val)) 
    (if (equal? key (caar dict))
      (cons (list key val) (cdr dict))
      (cons (list (caar dict) (car (cdar dict))) (set (cdr dict) key val))
    )
  )
  ; END PROBLEM 15
  )

;; Problem 16

;; implement solution-code
(define (solution-code problem solution)
  (cond ((null? problem) nil)
        ((equal? problem '_____) solution)
        ((pair? problem)
         (cons (solution-code (car problem) solution)
               (solution-code (cdr problem) solution)))
        (else problem)))
