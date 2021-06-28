# Consumption manager tests

## Reading and writing internal values

Take me to [error](#triggering-error)

**Author**: Maciej Marzecki

**Requirement ids**: [034.02.FW5]

**Test id**: 
tbd

**Test function name**: test_consumption_manager_internal_values
 
**Meter_features**:
- consumption manager
- irda
- lbus
- errors

**Description**: 

It must be possible for test to write and readout all internal values 
(e.g. current state of consumer accu) from all used consumption manager 
variables in production mode and field mode (with testflag)


**Specification**:
- Preconditions:
  - prepare a list of commands used to get and set internal values 
  - get a dictionary of all commands and privileges from command file
        
- Test_steps:

These steps should be repeated for production mode and field fallback mode with different roles

| # | Step |
| :---: | :---: |
| 1 | go to production or field fallback mode |
| 2 | change role to one of the possible if in field fallback mode |
| 3 | for every command from commands to test: |
| 3.1 | try to execute 'get' command and save the result |
| 3.2 | try to execute 'set' command with the previously saved value as parameter |

- Postconditions:
  - Go back to production mode
  - assert results

**Expected results**: 

All the commands used for getting or setting internal values connected to consumption manager
should work as specified in command file (in production mode all should work).

**Questions**: 

- List of all commands connected to consumption manager needed.
- Should we put this case in commands and privileges topic? Will there be such topic?


## Triggering error

**Author**: Maciej Marzecki

**Requirement ids**: [019.01.FW3], [034.02.FW2], [034.02.FW3], [034.02.FW4]

**Test id**: 
tbd

**Test function name**: test_consumption_manager_trigger_error
 
**Meter_features**:
- errors
- consumption manager
- irda
- lbus
- zvei

**Description**: 

The consumption manager shall trigger an error if consumption budget is risen by 
any of the consumers: LBUS, IRDA, ZVEI (if implemented). After exceeding the threshold 
communication via consumer should be blocked.


**Specification**:
- Preconditions:
  - Meter must be in field fallback mode
  - All consumer accus must be empty
  - There should be no consumption manager related error already on meter
        
- Test_steps:

These steps should be repeated for all SHARKY FS consumers (LBUS, IRDA, ZVEI (if implemented))

| # | Step |
| :---: | :---: |
| 1 | configure consumption manager threshold to value x |
| 2 | generate less then x traffic for one of the consumers |
| 3 | get meter errors |
| 4 | try to communicate via consumer | 
| 5 | generate as much traffic to fill consumers accu to x |
| 6 | get meter errors |
| 7 | try to communicate via consumer | 
| 8 | wait as much time as it is needed for consumption manager to regenerate |
| 9 | get meter errors |
| 10 | try to communicate via consumer | 

- Postconditions:
  - Go back to production mode
  - Reset consumer accus
  - Reset meter errors
  - assert results

**Expected results**: 

These results apply to all the consumers (LBUS, IRDA, ZVEI)
- while consumer accu is filled with less then x traffic there should be no consumption manager related error 
and communication via consumer should be possible
- when consumer accu is filled with exactly x traffic there should be consumption manager related error 
and communication via consumer should not be possible
- after regeneration time has passed there should be once more no consumption manager related error 
and communication via consumer should be possible once again

**Questions**: 

None


## L-Bus cyclic communication

**Author**: Maciej Marzecki

**Requirement ids**: [034.01.FW1]

**Test id**: 
tbd

**Test function name**: test_consumption_manager_lbus_communication 
 
**Meter_features**:
- consumption manager
- lbus

**Description**: 

The consumption manager configuration for L-Bus shall enable cyclic communications requests of INT9.


**Specification**:
- Preconditions:
  - Meter must be in field fallback mode
  - All consumer accus must be empty
  - There should be no consumption manager related error already on meter
        
- Test_steps:

| # | Step |
| :---: | :---: |
| 1 | configure lbus consumption manager |
| 2 | check cyclic communications requests of INT9 |

- Postconditions:
  - Go back to production mode
  - Reset consumer accus
  - Reset meter errors
  - assert results

**Expected results**: 

- tbd

**Questions**: 

- What does 'cyclic communications requests of INT9' mean?


## IrDA log readout

**Author**: Maciej Marzecki

**Requirement ids**: [034.01.FW2]

**Test id**: 
tbd

**Test function name**: test_consumption_manager_irda_log_readout
 
**Meter_features**:
- consumption manager
- irda
- metrological log

**Description**: 

The consumption manager configuration for IrDA communication shall enable readout of each log.

**Specification**:
- Preconditions:
  - Meter must be in field fallback mode
  - All consumer accus must be empty
  - There should be no consumption manager related error already on meter
  - There should be a dummy log created in each metrological log
        
- Test_steps:

| # | Step |
| :---: | :---: |
| 1 | try to read dummy log from each metrological log |
| 2 | configure irda consumption manager |
| 3 | try to read dummy log from each metrological log |

- Postconditions:
  - Go back to production mode
  - delete metrological log contents 
  - assert results

**Expected results**: 

- before irda consumption manager configuration reading logs form metrological log should not be possible
- after irda consumption manager configuration reading logs form metrological log should be possible

**Questions**: 

- What does 'readout of each log' mean?
- Before irda consumption manager configuration reading logs form metrological log should not be possible?


## Consumption manager on flow sensor

**Author**: Maciej Marzecki

**Requirement ids**: [034.02.FW1]

**Test id**: 
tbd

**Test function name**: test_consumption_manager_on_flow_sensor
 
**Meter_features**:
- consumption manager

**Description**: 

The flow sensor shall have a consumption manager

**Specification**:
- Preconditions:
  - Meter must be in field fallback mode
  - All consumer accus must be empty
  - There should be no consumption manager related error already on meter
        
- Test_steps:

    | # | Step |
    | :---: | :---: |
    | 1 | ????????????????????????????????????????? \\
    ??????????????????????? \
    ????????????????????????\
    ?????????????????????????\\|
    | 2 | ??? |

- Postconditions:
  - Go back to production mode
  - assert results

**Expected results**: 

- ???

**Questions**: 

- Requirement unclear.
