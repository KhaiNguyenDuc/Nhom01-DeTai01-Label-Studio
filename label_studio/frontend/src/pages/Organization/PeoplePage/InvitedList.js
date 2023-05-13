import { formatDistance } from "date-fns";
import { React ,useCallback, useEffect, useState } from "react";
import { Pagination, Spinner, Userpic } from "../../../components";
import { usePage, usePageSize } from "../../../components/Pagination/Pagination";
import { useAPI } from "../../../providers/ApiProvider";
import {useCurrentUser} from "../../../providers/CurrentUser";
import { Block, Elem } from "../../../utils/bem";
import { isDefined } from "../../../utils/helpers";
import { useUpdateEffect } from "../../../utils/hooks";
import './PeopleList.styl';
import { CopyableTooltip } from '../../../components/CopyableTooltip/CopyableTooltip';

export const InvitedList = () => {

    const api = useAPI();
    const [user, setUser] = useState();
    const [invitedList, setInvitedList] = useState();
    const [currentPage] = usePage('page', 1);
    const [currentPageSize] = usePageSize('page_size', 30);
    const [totalItems, setTotalItems] = useState(0);
    
    const fetchCurrentUser = useCallback(() => 
    {
      api.callApi('me').then(async user =>
      {
        setUser(user);
        const response = await api.callApi('invitedmembers', {
            params: {
              pk: user.active_organization,
              currentPage,
              page_size: currentPageSize,
            },
        });
        console.log(response)
          if (response.results) {
            setInvitedList(response.results);
            setTotalItems(response.count);
          }
      }, []);
    }, []);
  
    useEffect(() => {
      fetchCurrentUser();
    }, []);

  return (
    <>
      <Block name="people-list">
        <Elem name="wrapper">
          {invitedList ? (
            <Elem name="users">
              <Elem name="header">
                <Elem name="column" mix="avatar"/>
                <Elem name="column" mix="email_iv">Email</Elem>
                <Elem name="column" mix="role_iv">Role</Elem>
                <Elem name="column" mix="last-activity">Invited At</Elem>
              </Elem>
              <Elem name="body">
                {invitedList.map(({id, organization, email, role_name, invited_at}) => {
                  return (

                    <Elem key={`invite-${id}`}  name="user" >
                      <Elem name="field" mix="avatar">{id}</Elem>
                      <Elem name="field" mix="email_iv">
                        {email}
                      </Elem>
                      <Elem name="field" mix="role_iv">
                        {role_name}
                      </Elem>
                      <Elem name="field" mix="last-activity">
                        {formatDistance(new Date(invited_at), new Date(), { addSuffix: true })}
                      </Elem>
                    </Elem>
                  );
                })}
              </Elem>
            </Elem>
          ) : (
            <Elem name="loading">
              <Spinner size={36}/>
            </Elem>
          )}
        </Elem>
        
        <Pagination
          page={currentPage}
          urlParamName="page"
          totalItems={totalItems}
          pageSize={currentPageSize}
          pageSizeOptions={[30, 50, 100]}
          onPageLoad={fetchCurrentUser}
          style={{ paddingTop: 16 }}
        />
      </Block>
    </>
  );
};
