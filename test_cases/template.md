# Test name

**Author**: Peter Roth

**Requirement ids**: 
- R123
- R456

**Test id**: 
'afeefcc8-7de8-4dd7-94a6-a5571f3b1d17'

**Test function name**: test_pulse_output_2
 
**Meter_features**:
- pulses
- flow_simulation

**Date of last change**: 22.06.2021

**Changed by**: Robert Hirschmann

**Description**: This is a fancy description

**Specification**:
- Preconditions:
  - Meter must be in production mode
  - Exception recorder must be empty
  - Volume accus must be set to zero
        
- Test_steps:
1. Activate pulse output 2
2. Activate simulated volume
3. Wait 3 minutes
4. Get pulses count

- Postconditions:
  - Reset exception recorder
  - Reset volume accus 

**Expected result**: Number of pulses counted should increase