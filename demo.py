"""Offline walkthrough of actual use cases. No simulated LLM quality scores."""
import json
from app.storage import Storage
from app.service import Service,DemoClient
from app.bot import card

with_db=Storage()
try:
    with_db.set_zone(1,'Europe/Moscow')
    service=Service(with_db,DemoClient())
    draft=service.propose(1,'Завтра в 15:00 встреча с Андреем, на обед борщ, не забыть оплатить интернет, потратил 550 на такси')
    print('OFFLINE DEMO: локальные правила, не внешний LLM\n'+card(draft))
    draft=service.edit(1,draft['id'],3,{'amount':500},draft['revision'])
    ids=with_db.confirm(1,draft['id'],draft['revision'])
    print('\nПодтверждены записи:',ids)
    assert with_db.confirm(1,draft['id'],draft['revision'])==ids
    print('Повторное подтверждение: дубликатов нет')
    print('Сегодня:',len(service.feed(1,'today')['records']))
    print('В истории:',len(service.feed(1,'history')['records']))
    print('Метрики (не пилот):',json.dumps(with_db.metrics(),ensure_ascii=False))
finally: with_db.close()
