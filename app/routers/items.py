import logging
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix='/items',
    tags=['Items']
)

fake_itesm_db = {'apple' : {'name' : 'Apple', 'price' : 5},
                  'banana' : {'name' : 'Banana', 'price' : 8}  }

@router.get("")
async def get_items():
    logging.info("METHOD : get_items ROUTER : Items")
    return fake_itesm_db


@router.get('/{item_id}')
async def get_item_by_id(item_id : str):
    
    if item_id not in fake_itesm_db:
        logging.error(",ROUTER : Items METHOD : get_item_by_id Item_Id : %s", item_id)
        raise HTTPException(status_code=404, detail='Item not found')
    else:
        logging.info(",ROUTER : Items METHOD : get_item_by_id Item_Id : %s", item_id)
        return fake_itesm_db[item_id]


