# FEEZ-BUZZ

## config file:

    class Config:
        MAX = 50                    # the limit of default iteration 
        SEPARATOR = ', '            # separator in the output
        SUB_SEPARATOR = "-"         # separator Between FEEZ and BUZZ for 15, 30 ... 
        END_OUTPUT = "."            # Character at least of the output
        
        # divisors is a dict with k = divisor, value = output or function
        # k can't be 0 or other than int.
        DIVISORS = {
            # 0:"AIE!", #-> FORBIDEN !
            3: {
                "output":"FEEZ",
                "func": lambda x : x*x
            },
            5: {
                "output":"BUZZ",
                "func": lambda x : x+x
            }
        }
        # Default list to handle.
        DEFAULT_ITERABLE = range(1,MAX+1)
        DEFAULT_IS_SIMPLE_OUTPUT = True


## Run

    python main.py

ou

    make run # see Makefile below.

## Output or Func:

In the config file :

    default_output_choice = True    # output (1,2,FEEZ ...)
    default_output_choice = False   # function(n)

## Makefile

     _______________________________________________
    |   Commands        |          Actions          |
    |-------------------|---------------------------|
    | make help  ------ | ------> Show this help.   |
    | make run   ------ | ------> Run the app.      |
    | make test  ------ | ------> Run unit tests.   |
    | make clean ------ | ------> Clean the cache.  |
    |_______________________________________________|