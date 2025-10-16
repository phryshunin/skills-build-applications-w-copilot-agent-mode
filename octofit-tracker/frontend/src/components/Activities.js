import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Activities endpoint:', endpoint);
        console.log('Fetched activities:', data);
        setActivities(data.results || data);
      });
  }, [endpoint]);

  return (
    <div>
      <h2>Activities</h2>
      <ul className="list-group">
        {activities.map((activity, idx) => (
          <li key={idx} className="list-group-item">
            {activity.activity_type} - {activity.duration_minutes} min - {activity.points} pts
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;
