(define (domain Guarinis_domain)
(:requirements :strips :typing :negative-preconditions)
(:predicates
    (at ?figure ?row ?col)
    (diff_by_one ?row ?col)
    (diff_by_two ?row ?col)
    (clean ?row ?col)
)
(:action knight_move
    :parameters (
        ?knight
        ?from_row ?from_col ?to_row ?to_col
    )
    :precondition (and 
        (clean ?to_row ?to_col)
        (at ?knight ?from_row ?from_col)
        (or
            (and
                (diff_by_two ?from_row ?to_row)
                (diff_by_one ?from_col ?to_col)
            )
            (and 
                (diff_by_one ?from_row ?to_row)
                (diff_by_two ?from_col ?to_col)
            )
        )
    )
    :effect (and
            (not (at ?knight ?from_row ?from_col))
            (at ?knight ?to_row ?to_col)
            (not (clean ?to_row ?to_col))
            (clean ?from_row ?from_col) 
    )
)
)