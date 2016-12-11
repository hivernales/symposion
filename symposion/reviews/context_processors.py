from symposion.conference.models import current_conference
from symposion.proposals.models import ProposalSection


def reviews(request):
    sections = []
    conf = current_conference()
    for section in ProposalSection.objects.filter(section__conference=conf):
        if request.user.has_perm("reviews.can_review_%s" % section.section.slug):
            sections.append(section)
    return {
        "review_sections": sections,
    }
