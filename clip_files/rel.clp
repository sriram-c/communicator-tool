
;interchanging not rel with verb
;mEM nahIM jA sakawA
(defrule neg_rule
?f<-(user_discourse_rel-ids  neg  ?v  ?neg)
=>
	(retract ?f)
	(assert (user_inter_chunk_rel-ids neg ?neg ?v))
)
