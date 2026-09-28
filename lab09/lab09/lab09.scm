(define (over-or-under num1 num2) 
    (cond ((> num1 num2) 1)
          ((= num1 num2) 0)
          ((< num1 num2) (- 0 1))
    )
)

(define (composed f g) 
    (lambda (x) (f (g x)))
)

(define (repeat f n)
  (if (= n 0)
      (lambda (x) x)           
      (composed f (repeat f (- n 1)))))

(define lst 
    (list (cons 1 nil) 2 (cons 3 (cons 4 nil)) 5)
)

(define (without-duplicates lst)
  (if (null? lst)
      nil
      (cons (car lst)
            (without-duplicates
              (filter (lambda (x) (not (= x (car lst)))) (cdr lst))))))
