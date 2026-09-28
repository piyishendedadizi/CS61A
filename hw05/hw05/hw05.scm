(define (square n) (* n n))

(define (pow base exp)
  (cond ((= exp 0) 1)
        ((even? exp) (square (pow base (/ exp 2))))
        (else (* base (square (pow base (/ (- exp 1) 2)))))))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (begin (define y (- n 1)) (repeatedly-cube y (* x (* x x))))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))
