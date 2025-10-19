# FEEZ-BUZZ

## config file:

    class Config:
        MAX = 50                    # the limit of default iteration 
        SEPARATOR = ', '            # separator in the output
        SUB_SEPARATOR = "-"         # separator Between FEEZ and BUZZ for 15, 30 ... 
        END_OUTPUT = "."            # Character at least of the output
        
        # divisors is a dict with k = divisor, value = output or function
        # k can't be 0 or other than int.
        DIVISORS_KEYS = ["output","func"]
        DIVISORS = {
            # 0:"AIE!", #-> FORBIDEN !
            3: {
                f"{DIVISORS_KEYS[0]}":"FEEZ",
                f"{DIVISORS_KEYS[1]}": lambda x : x*x
            },
            5: {
                f"{DIVISORS_KEYS[0]}":"BUZZ",
                f"{DIVISORS_KEYS[1]}": lambda x : x+x
            }
        }
        # Default list to handle.
        DEFAULT_ITERABLE = range(1,MAX+1)
        DEFAULT_IS_SIMPLE_OUTPUT = True


## Run

    python main.py

or

    make run    # see Makefile below.

## Unit Tests

    pytest -v

or

    make test   # see Makefile below.

## Makefile

     _______________________________________________
    |   Commands        |          Actions          |
    |-------------------|---------------------------|
    | make help  ------ | ------> Show this help.   |
    | make run   ------ | ------> Run the app.      |
    | make test  ------ | ------> Run unit tests.   |
    | make clean ------ | ------> Clean the cache.  |
    |_______________________________________________|