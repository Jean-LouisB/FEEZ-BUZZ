# FEEZ-BUZZ

## config file:

    class Config:
    max = 50                    # the limit of default iteration 
    sep = ', '                  # separator in the output
    sep_multiple_output = "-"   # separator Between FEEZ and BUZZ for 15, 30 ... 
    end = "."                   # Character at least of the output
    
    # divisors is a dict with k = divisor, value = output or function
    # k can't be 0 or other than int.
    divisors = {
        #0:"AIE!", -> FORBIDEN !
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
    default_iterable = range(1,max+1)
    default_output_choice = True

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