from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class AqaraDoorAndWindowSensor(AliceSkill):
	"""
	Author: Psychokiller1888
	Description: Connect your aqara door and window sensors to alice. requires zigbee2mqtt
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
