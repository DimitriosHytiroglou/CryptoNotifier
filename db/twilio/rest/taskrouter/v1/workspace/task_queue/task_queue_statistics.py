# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class TaskQueueStatisticsList(ListResource):
    """  """

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsList
        """
        super(TaskQueueStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'task_queue_sid': task_queue_sid,
        }

    def get(self):
        """
        Constructs a TaskQueueStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsContext
        """
        return TaskQueueStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __call__(self):
        """
        Constructs a TaskQueueStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsContext
        """
        return TaskQueueStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueStatisticsList>'


class TaskQueueStatisticsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the TaskQueueStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsPage
        """
        super(TaskQueueStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskQueueStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsInstance
        """
        return TaskQueueStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueStatisticsPage>'


class TaskQueueStatisticsContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsContext
        """
        super(TaskQueueStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'task_queue_sid': task_queue_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/Statistics'.format(**self._solution)

    def fetch(self, end_date=values.unset, minutes=values.unset,
              start_date=values.unset, task_channel=values.unset,
              split_by_wait_time=values.unset):
        """
        Fetch a TaskQueueStatisticsInstance

        :param datetime end_date: The end_date
        :param unicode minutes: The minutes
        :param datetime start_date: The start_date
        :param unicode task_channel: The task_channel
        :param unicode split_by_wait_time: The split_by_wait_time

        :returns: Fetched TaskQueueStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsInstance
        """
        params = values.of({
            'EndDate': serialize.iso8601_datetime(end_date),
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskChannel': task_channel,
            'SplitByWaitTime': split_by_wait_time,
        })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return TaskQueueStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueStatisticsContext {}>'.format(context)


class TaskQueueStatisticsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsInstance
        """
        super(TaskQueueStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'cumulative': payload['cumulative'],
            'realtime': payload['realtime'],
            'task_queue_sid': payload['task_queue_sid'],
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid,
            'task_queue_sid': task_queue_sid,
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: TaskQueueStatisticsContext for this TaskQueueStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsContext
        """
        if self._context is None:
            self._context = TaskQueueStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                task_queue_sid=self._solution['task_queue_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def cumulative(self):
        """
        :returns: The cumulative
        :rtype: dict
        """
        return self._properties['cumulative']

    @property
    def realtime(self):
        """
        :returns: The realtime
        :rtype: dict
        """
        return self._properties['realtime']

    @property
    def task_queue_sid(self):
        """
        :returns: The task_queue_sid
        :rtype: unicode
        """
        return self._properties['task_queue_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, end_date=values.unset, minutes=values.unset,
              start_date=values.unset, task_channel=values.unset,
              split_by_wait_time=values.unset):
        """
        Fetch a TaskQueueStatisticsInstance

        :param datetime end_date: The end_date
        :param unicode minutes: The minutes
        :param datetime start_date: The start_date
        :param unicode task_channel: The task_channel
        :param unicode split_by_wait_time: The split_by_wait_time

        :returns: Fetched TaskQueueStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics.TaskQueueStatisticsInstance
        """
        return self._proxy.fetch(
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueStatisticsInstance {}>'.format(context)
