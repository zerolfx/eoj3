from django.conf.urls import url

from polygon.problem.views import base, asset, case, program, revision, statement

urlpatterns = [
    url(r'^$', base.ProblemList.as_view(), name='problem_list'),
    url(r'^create/$', base.ProblemCreate.as_view(), name='problem_create'),

    url(r'^(?P<pk>\d+)/revision/create/$', revision.RevisionCreateView.as_view(), name='revision_create'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/$', revision.RevisionUpdateView.as_view(), name='revision_view'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/fork/$', revision.RevisionForkView.as_view(), name='revision_fork'),

    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/asset/$', asset.AssetList.as_view(), name='revision_asset'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/asset/create/$', asset.AssetCreateView.as_view(),
        name='revision_asset_create'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/asset/(?P<apk>\d+)/update/$', asset.AssetUpdateView.as_view(),
        name='revision_asset_update'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/asset/(?P<apk>\d+)/rename/$', asset.AssetRenameView.as_view(),
        name='revision_asset_rename'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/asset/(?P<apk>\d+)/delete/$', asset.AssetDeleteView.as_view(),
        name='revision_asset_delete'),

    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/statement/$', statement.StatementList.as_view(),
        name='revision_statement'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/statement/create/$', statement.StatementCreateView.as_view(),
        name='revision_statement_create'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/statement/(?P<spk>\d+)/update/$', statement.StatementUpdateView.as_view(),
        name='revision_statement_update'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/statement/(?P<spk>\d+)/activate/$',
        statement.StatementActivateView.as_view(),
        name='revision_statement_activate'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/statement/(?P<spk>\d+)/delete/$', statement.StatementDeleteView.as_view(),
        name='revision_statement_delete'),

    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/program/$', program.ProgramList.as_view(), name='revision_program'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/program/create/$', program.ProgramCreateView.as_view(),
        name='revision_program_create'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/program/(?P<ppk>\d+)/update/$', program.ProgramUpdateView.as_view(),
        name='revision_program_update'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/program/(?P<ppk>\d+)/toggle/$', program.ProgramActiveToggleView.as_view(),
        name='revision_program_toggle'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/program/(?P<ppk>\d+)/delete/$', program.ProgramDeleteView.as_view(),
        name='revision_program_delete'),

    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/case/$', case.CaseList.as_view(), name='revision_case'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/case/create/$', case.CaseCreateView.as_view(),
        name='revision_case_create'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/case/(?P<cpk>\d+)/update/info/$', case.CaseUpdateInfoView.as_view(),
        name='revision_case_update_info'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/case/(?P<cpk>\d+)/update/$', case.CaseUpdateFileView.as_view(),
        name='revision_case_update_file'),
    url(r'^(?P<pk>\d+)/revision/(?P<rpk>\d+)/case/(?P<cpk>\d+)/delete/$', case.CaseDeleteView.as_view(),
        name='revision_case_delete'),
]
