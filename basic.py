from classdef import db,Puppies,Owners,Toys

rufus=Puppies('Rufus')
fido=Puppies('Fido')
db.session.add_all([rufus,fido])
db.session.commit()

print(Puppies.query.all())

rufus=Puppies.query.filter_by(name='Rufus').first()


owner1=Owners('Owner1',rufus.id)
toy1=Toys('Chewtoy',rufus.id)
toy2=Toys('Ball',rufus.id)
db.session.add_all([owner1,toy1,toy2])
db.session.commit()

rufus=Puppies.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_of_toys()
