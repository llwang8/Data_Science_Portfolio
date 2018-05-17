import pandas as pd

enrollment = pd.read_csv('data/CRDC2013_14.csv', encoding='latin-1')

# Gender Profile in School
enrollment['total_enrollment'] = enrollment['TOT_ENR_M'] + enrollment['TOT_ENR_F']

all_enrollment = enrollment['total_enrollment'].sum()

print('--- Gender Profile in School ---')

M_ratio = enrollment['TOT_ENR_M'].sum() / all_enrollment * 100
print('Male:  {0:.2f} %'.format(M_ratio))
F_ratio = enrollment['TOT_ENR_F'].sum() / all_enrollment * 100
print('Female:  {0:.2f} %'.format(F_ratio))

# Race Composition in School
print('--- Race Composition in School ---')

enrollment['HI'] = enrollment['SCH_ENR_HI_M'] + enrollment['SCH_ENR_HI_F']
hispanic_ratio = enrollment['HI'].sum() / all_enrollment * 100
print('Hispanic:  {0:.2f} %'.format(hispanic_ratio))


enrollment['AM'] = enrollment['SCH_ENR_AM_M'] + enrollment['SCH_ENR_AM_F']
AM_ratio = enrollment['AM'].sum() / all_enrollment * 100
print('American Indian:  {0:.2f} %'.format(AM_ratio))


enrollment['AS'] = enrollment['SCH_ENR_AS_M'] + enrollment['SCH_ENR_AS_F']
asian_ratio = enrollment['AS'].sum() / all_enrollment * 100
print('Asian:  {0:.2f} %'.format(asian_ratio))

      
enrollment['HP'] = enrollment['SCH_ENR_HP_M'] + enrollment['SCH_ENR_HP_F']
HP_ratio = enrollment['HP'].sum() / all_enrollment * 100
print('Hawaiian / Pacific Islander:  {0:.2f} %'.format(HP_ratio))


enrollment['BL'] = enrollment['SCH_ENR_BL_M'] + enrollment['SCH_ENR_BL_F']
black_ratio = enrollment['BL'].sum() / all_enrollment * 100
print('Black:  {0:.2f} %'.format(black_ratio))


enrollment['WH'] = enrollment['SCH_ENR_WH_M'] + enrollment['SCH_ENR_WH_F']
white_ratio = enrollment['WH'].sum() / all_enrollment * 100      
print('White:  {0:.2f} %'.format(white_ratio))
      
      
enrollment['TR'] = enrollment['SCH_ENR_TR_M'] + enrollment['SCH_ENR_TR_F']
TR_ratio = enrollment['TR'].sum() / all_enrollment * 100
print('Two or More Races:  {0:.2f} %'.format(TR_ratio))


# Gender and race differrnces in SAT Scores 
print('SAT Score Average Difference for Different Races')

enrollment['SAT_HI'] = enrollment['SCH_SATACT_HI_M'] + enrollment['SCH_SATACT_HI_F']
avg_SAT_HI = enrollment['SAT_HI'].sum() / enrollment['HI'].sum()
print('Hispanics:  {0:.2f}'.format(avg_SAT_HI))


enrollment['SAT_AS'] = enrollment['SCH_SATACT_AS_M'] + enrollment['SCH_SATACT_AS_F']
avg_SAT_AS = enrollment['SAT_AS'].sum() / enrollment['AS'].sum()
print('Asians:  {0:.2f}'.format(avg_SAT_AS))



