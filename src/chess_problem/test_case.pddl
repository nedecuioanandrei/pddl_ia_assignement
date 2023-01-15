(define (problem test_case) (:domain Guarinis_domain)
(:objects 
    n1 n2 n3
    b_k_1 b_k_2 w_k_1 w_k_2
)

(:init
    (at b_k_1 n1 n3)
    (at b_k_2 n3 n3)
    (at w_k_2 n3 n1)
    (at w_k_1 n1 n1)
    (diff_by_one n1 n2)
    (diff_by_one n2 n1)
    (diff_by_one n2 n3)
    (diff_by_one n3 n2)
    (diff_by_two n1 n3)
    (diff_by_two n3 n1)
    (clean n1 n2)
    (clean n2 n1)
    (clean n2 n2)
    (clean n2 n3)
    (clean n3 n2)
)

(:goal (and
    (and
        (at w_k_2 n1 n3)
        (at w_k_1 n3 n3)
        (at b_k_2 n1 n1)
        (at b_k_1 n3 n1)
    )
))
)
