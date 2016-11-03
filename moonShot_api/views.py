'''
Created on Oct 29, 2016

@author: alexei.minin
'''

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from moonShot_api.serializers import DrawSerializer, LotterySerializer
from moonShot_structure.models import Lottery, Draw
from rest_framework.response import Response

class DrawViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing draws.
    """
    queryset = Draw.objects.all()
    serializer_class = DrawSerializer
    permission_classes = [AllowAny]
    
    #update lottery filed in draw model.
    def update(self, request, pk=None):
        try:
            draw_obj = self.queryset.get(id = pk)
            new_lottery = request.data.get('lottery')
            draw_obj.lottery_id = new_lottery
            draw_obj.save()
            json_data = self.serializer_class(draw_obj)
            return Response(json_data.data)
        except Exception as e:
            raise
    
class LotteryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing lotteries.
    """
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer
    permission_classes = [AllowAny]

'''    
def celery_test(request):
    import requests
    import xmltodict
    response = requests.get('{url}'.format(url = 'http://www.lotteryfeed.com/xml_b/all_jackpots.xml'), stream=True)
    xml_obj = xmltodict.parse(response.content)
    for root_tag, games_dict in xml_obj.items():
        for jackpots, list_of_games in games_dict.items():
            for games in list_of_games:
                _state = games.values()
                draw_title = _state[0]                    
                for game in games.get("game_jackpot"):
                    _game = game.values()
                    lottery_title = _game[0]
                    lottery_id = _game[1]
                    next_draw = _game[3].values()[0].values()[3]                
                    draw_date = _game[5].values()[0].values()[3]
                    try:
                        lott_obj, status = Lottery.objects.get_or_create(title = lottery_title)
                        draw_obj, status = Draw.objects.update_or_create(lottery_id = lott_obj.id,
                                                                                title = draw_title,
                                                                                jackpot = next_draw,
                                                                                date = draw_date
                                                                                   )
                    except Exception as e:
                        print str(e)
'''