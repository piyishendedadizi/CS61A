(define (accumulate merger start n term)
  (if (= n 0)
      start
      (accumulate merger (merger start (term n)) (- n 1) term)))

(define (accumulate-tail merger start n term)
  (if (= n 0)
      start
      (accumulate merger (merger start (term n)) (- n 1) term)))