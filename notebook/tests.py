from unittest import TestCase
from . import models


class ContactTestCase(TestCase):
    def setUp(self):
        contacts = models.Contact.objects.all()
        for c in contacts:
            c.delete()
        self.contact = models.Contact.objects.create(name="foo", email="foo@algolia.com")
        self.account1 = models.Account.objects.create(username="test@x.com", service="X")
        self.account2 = models.Account.objects.create(username="test@y.com", service="Y")
        self.contact.accounts.add(self.account1, self.account2)

    def test_Contacts_account_ids(self):
        """Contacts expose the correct account ids """
        foo = models.Contact.objects.get(name="foo")
        ids = foo.account_ids()
        self.assertEqual(len(ids), 2)
        self.assertTrue(self.account1.id in ids)
        self.assertTrue(self.account2.id in ids)

    def test_Contacts_account_names(self):
        """Contacts expose the correct account names """
        foo = models.Contact.objects.get(name="foo")
        names = foo.account_names()
        self.assertEqual(len(names), 2)
        self.assertTrue('test@x.com@X' in names)
        self.assertTrue('test@y.com@Y' in names)
