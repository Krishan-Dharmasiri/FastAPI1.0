from datetime import date

def add_leading_zero(value : str)-> str:
    if len(value) == 1 : 
        return '0' + value
    else:  
        return value
    
def get_today_with_underscores()-> str:
    '''
        Returns the date part with underscoores with the format year_month_day
    '''
    return f"{str(date.today().year)}_{add_leading_zero(str(date.today().month))}_{add_leading_zero(str(date.today().day))}"