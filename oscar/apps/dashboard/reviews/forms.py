from django import forms
from django.db.models import get_model
from django.utils.translation import ugettext_lazy as _

ProductReview = get_model('reviews', 'productreview')


class DashboardProductReviewForm(forms.ModelForm):
    choices= (
        (ProductReview.APPROVED, _('Approved')),
        (ProductReview.REJECTED, _('Rejected')),
    )
    status = forms.ChoiceField(choices=choices)

    class Meta:
        model = ProductReview
        fields = ('title', 'body', 'score', 'status')


class ProductReviewSearchForm(forms.Form):
    STATUS_CHOICES = (
        ('', '------------'),
    ) + ProductReview.STATUS_CHOICES
    keyword = forms.CharField(required=False)
    status = forms.ChoiceField(required=False, choices=STATUS_CHOICES)
    date_from = forms.DateTimeField(required=False)
    date_to = forms.DateTimeField(required=False, label=_('to'))
    name = forms.CharField(required=False)

    def get_friendly_status(self):
        raw = int(self.cleaned_data['status'])
        for key, value in self.STATUS_CHOICES:
            if key == raw:
                return value
        return ''
