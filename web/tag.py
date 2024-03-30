import datetime
import model
import service.tag as service

@app.post('/')
def create(tag_in: model.tag.TagIn) -> model.tag.TagIn:
    tag: model.tag.Tag = model.tag.Tag(tag=tag_in.tag, created=datetime.datetime.now(datetime.timezone.utc),
        secret="shhhh")
    service.create(tag)
    return tag_in
@app.get('/{tag_str}', response_model=model.tag.TagOut)
def get_one(tag_str: str) -> model.tag.TagOut:
    tag: model.tag.Tag = service.get(tag_str)
    return tag