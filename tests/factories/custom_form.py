import factory

import tests.factories.common as common
from tests.factories.event import EventFactoryBasic
from app.models.custom_form import CustomForms, db


class CustomFormFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = CustomForms
        sqlalchemy_session = db.session

    event = factory.RelatedFactory(EventFactoryBasic)
    form = common.string_
    field_identifier = common.string_
    type = "text"
    is_required = False
    is_included = False
    is_fixed = False
    event_id = 1
